import flask
import os
import sqlite3

print(os.path.isfile('server.py'))

def get_db():
    db = sqlite3.connect(
        r'C:\Users\Beertino\Desktop\Github\h2-web-dev\Blogger Starter\db.sqlite3')
    # db = sqlite3.connect('db.sqlite3')
    db.row_factory = sqlite3.Row
    return db


def create_db():
    db = get_db()
    db.execute('CREATE TABLE post ' +
               '(id INTEGER PRIMARY KEY AUTOINCREMENT, ' +
               'title TEXT NOT NULL, ' +
               'body TEXT, ' +
               'image TEXT, ' +
               'file TEXT)')
    db.close()


if not os.path.isfile('db.sqlite3'):
    create_db()
