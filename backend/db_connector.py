#!/usr/bin/env python3
from typing import List, Dict, Callable, Any
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import datetime
from datetime import timedelta

JSON = List[Dict[str: Any]]

app = Flask(__name__)

# Origin cors
CORS(app)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql://root:123456789@localhost/calendar'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

ma = Marshmallow(app)


class Tasks(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    title: str = db.Column(db.String(255))
    startDate: str = db.Column(db.DateTime)
    endDate: str = db.Column(db.DateTime)
    rRule: str = db.Column(db.String(255))
    allDay: bool = db.Column(db.Boolean)

    def __init__(self, title, startDate, endDate, allDay):
        self.title = title
        self.startDate = startDate
        self.endDate = endDate
        self.allDay = allDay


class TasksSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'startDate',
                  'endDate', 'rRule', 'allDay')


task_schema = TasksSchema()
tasks_schema = TasksSchema(many=True)


@app.route('/get', methods=['GET'])
def get_tasks() -> JSON:
    """
    Gets all tasks from database
    :return: tasks
    """
    all_tasks = Tasks.query.all()
    results = tasks_schema.dump(all_tasks)
    return jsonify(results)


@app.route('/get/<id>', methods=['GET'])
def get_task(taskID) -> JSON:
    """
    Gets single task out of database
    :param taskID: ID of task in database
    :return:
    """
    task = Tasks.query.get(taskID)
    return task_schema.jsonify(task)


@app.route('/update/<id>', methods=['PUT'])
def update_task(taskID) -> Callable:
    """
    Updates task in database
    :param taskID: ID of task in database
    :return:
    """
    task = Tasks.query.get(taskID)
    if 'title' in request.json:
        title = request.json['title']
        task.title = title
    if 'allDay' in request.json:
        allDay = request.json['allDay']
        task.allDay = allDay
    if 'startDate' in request.json:
        startDate = datetime.strptime(request.json['startDate'],
                                      '%Y-%m-%dT%H:%M:%S.%fZ')
        startDate = startDate + timedelta(hours=2)
        task.startDate = startDate
    if 'endDate' in request.json:
        endDate = datetime.strptime(request.json['endDate'],
                                    '%Y-%m-%dT%H:%M:%S.%fZ')
        endDate = endDate + timedelta(hours=2)
        task.endDate = endDate
    db.session.commit()
    return get_tasks()


@app.route('/delete/<id>', methods=['DELETE'])
def delete_task(taskID) -> Callable:
    """
    Deletes task from database.
    :param taskID: ID of task in database
    :return:
    """
    task = Tasks.query.get(taskID)
    db.session.delete(task)
    db.session.commit()
    return get_tasks()


@app.route('/add', methods=['POST'])
def add_task() -> Callable:
    """
    Adds task to database
    :return:
    """
    title = request.json['title']
    allDay = request.json['allDay']

    # '2022-05-07T00:00:24.404Z'
    startDate = datetime.strptime(
        request.json['startDate'], '%Y-%m-%dT%H:%M:%S.%fZ')
    endDate = datetime.strptime(
        request.json['endDate'], '%Y-%m-%dT%H:%M:%S.%fZ')

    # Added additional two hours due to time zones.
    startDate = startDate + timedelta(hours=2)
    endDate = endDate + timedelta(hours=2)

    tasks = Tasks(title, startDate, endDate, allDay)

    db.session.add(tasks)
    db.session.commit()
    return get_tasks()


if __name__ == '__main__':
    app.run(debug=True)
