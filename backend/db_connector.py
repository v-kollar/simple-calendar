from time import strftime
from tracemalloc import start
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import datetime
from datetime import datetime, timedelta

app = Flask(__name__)
#Origin cors
CORS(app)

# Databse configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456789@localhost/calendar'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

ma=Marshmallow(app)

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    startDate = db.Column(db.DateTime)
    endDate = db.Column(db.DateTime)
    rRule = db.Column(db.String(255))
    allDay = db.Column(db.Boolean)

    def __init__(self, title, startDate, endDate, allDay):
        self.title=title
        self.startDate=startDate
        self.endDate=endDate
        self.allDay=allDay


class TasksSchema(ma.Schema):
    class Meta:
        fields = ('id','title','startDate','endDate','rRule','allDay')

task_schema = TasksSchema()
tasks_schema = TasksSchema(many=True)

@app.route('/get', methods=['GET'])
def get_tasks():
    all_tasks = Tasks.query.all()
    results = tasks_schema.dump(all_tasks)
    return jsonify(results)

@app.route('/get/<id>', methods=['GET'])
def get_task(id):
    task = Tasks.query.get(id)
    return task_schema.jsonify(task)

@app.route('/update/<id>',methods = ['PUT'])
def update_task(id):
    task = Tasks.query.get(id)
    if('title' in request.json):
        title = request.json['title']
        task.title = title
    if('allDay' in request.json):
        allDay = request.json['allDay']
        task.allDay = allDay
    if('startDate' in request.json):
        startDate = datetime.strptime(request.json['startDate'], '%Y-%m-%dT%H:%M:%S.%fZ')
        startDate = startDate + timedelta(hours=2)
        task.startDate = startDate
    if('endDate' in request.json):
        endDate = datetime.strptime(request.json['endDate'], '%Y-%m-%dT%H:%M:%S.%fZ')
        endDate = endDate + timedelta(hours=2)
        task.endDate = endDate
    db.session.commit()
    return get_tasks()

@app.route('/delete/<id>',methods=['DELETE'])
def delete_task(id):
    task = Tasks.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return get_tasks()

@app.route('/add',methods=['POST'])
def add_task():
    title = request.json['title']
    allDay = request.json['allDay']

    #'2022-05-07T00:00:24.404Z'
    startDate = datetime.strptime(request.json['startDate'], '%Y-%m-%dT%H:%M:%S.%fZ')
    endDate = datetime.strptime(request.json['endDate'], '%Y-%m-%dT%H:%M:%S.%fZ')

    startDate = startDate + timedelta(hours=2)
    endDate = endDate + timedelta(hours=2)
    #Timezone
    tasks = Tasks(title, startDate, endDate, allDay)

    db.session.add(tasks)
    db.session.commit()
    return get_tasks()


if __name__=='__main__':
    app.run(debug=True)