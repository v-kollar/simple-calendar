from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
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

    def __init__(self,title,rRule,allDay):
        self.title=title
        self.rRule=rRule
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

    title = request.json['title']
    startDate = request.json['startDate']
    endDate = request.json['endDate']
    rRule = request.json['rRule']
    allDay = request.json['allDay']

    task.title = title
    task.startDate = startDate
    task.endDate = endDate
    task.rRule = rRule
    task.allDay = allDay

    db.session.commit()
    return task_schema.jsonify(task)

@app.route('/delete/<id>',methods=['DELETE'])
def delete_task(id):
    task = Tasks.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return task_schema.jsonify(task)

@app.route('/add',methods=['POST'])
def add_task():
    title = request.json['title']
    startDate = request.json['startDate']
    endDate = request.json['endDate']
    rRule = request.json['rRule']
    allDay = request.json['allDay']

    tasks = Tasks(title,startDate,endDate,rRule,allDay)
    db.session.add(tasks)
    db.session.commit()
    return task_schema.jsonify(tasks)

if __name__=='__main__':
    app.run(debug=True)