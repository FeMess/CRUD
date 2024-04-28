import sqlite3
import os

name_db = 'users.db'

def create_database():
    list_dir = os.listdir(os.getcwd())
    list_dir = [x.split('.')[1] for x in list_dir]

    if not 'db' in list_dir:
        connect = sqlite3.connect(name_db)
        connect.close()
    else:
        pass

def create_table(database_name = name_db):
    connect = sqlite3.connect(database_name)
    cursor = connect.cursor()

    sql_command = """CREATE TABLE clients (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                age INTEGER NOT NULL 
                )"""

    cursor.execute(sql_command)
    connect.commit()
    connect.close()
