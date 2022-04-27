#!/usr/bin/env python3
import mysql.connector
from typing import Callable

db = mysql.connector.connect(
    database="calendar",
    host="::1",
    user="admin",
    passwd="localhostapp."
)

def db_exec(command: str) -> Callable:
    db.cursor().execute(f"{command}")

def create_table(name: str) -> Callable:
    try:
        db.cursor().execute(f"CREATE TABLE {name}")
        print(f"Table {name} has been created.")
    except mysql.connector.DatabaseError:
        print("Table must have at least one column.")

def delete_table(name: str) -> Callable:
    try:
        db.cursor().execute(f"DROP TABLE {name}")
        print(f"Table {name} has been deleted.")
    except mysql.connector.Error:
        print(f"Can't create table '{name}', because it does not exist.")

# db_exec("CREATE TABLE user (name VARCHAR(255), surname VARCHAR(255))")