#!/usr/bin/env python3

from flask import Flask
from flask_restful import Api
import mysql.connector as mysql
from typing import Any  # Dict, List
import json

Action = Any
JSON = str  # List[Dict[str, Any]]

app = Flask(__name__)
api = Api(app)
# SELECT * FROM calendar.user

db = mysql.connect(
    database="calendar",
    host="::1",
    user="root",
    passwd="Rootroot.000"
)

cursor = db.cursor(dictionary=True)


def db_command(command: str) -> Action:
    """
    Executes commands via SQL queries.
    :param command:
    :return:
    """
    cursor.execute(f"{command}")


def create_table(name: str) -> Action:
    """
    Creates table in SQL database.
    :param name:
    :return:
    """
    try:
        cursor.execute(f"CREATE TABLE {name}")
        print(f"Table {name} has been created.")
    except mysql.DatabaseError as error:
        print(f"Something went wrong: {error}")


def delete_table(name: str) -> Action:
    """
    Deletes table in SQL database.
    :param name:
    :return:
    """
    try:
        cursor.execute(f"DROP TABLE {name}")
        print(f"Table {name} has been deleted.")
    except mysql.DatabaseError as error:
        print(f"Something went wrong: {error}")


# db_exec("CREATE TABLE calendar (id INTEGER, name VARCHAR(255))")

db_command('SELECT * FROM calendar.calendar')


@app.route('/')
def get_data() -> JSON:
    """
    Converts SQL data into JSON.
    :return: JSON
    """
    try:
        json_data = json.dumps(cursor.fetchall())
        return json_data
    except mysql.DatabaseError as error:
        print(f"Something went wrong: {error}")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
