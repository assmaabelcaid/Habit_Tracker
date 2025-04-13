import sqlite3
from datetime import date

def get_db(name="main.db"):

    db = sqlite3.connect('main.db')
    return db

def create_table(db):
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS counter (
        name TEXT primary key,
        description TEXT)""")

    cursor.execute(""" CREATE TABLE IF NOT EXISTS tracker (
    date text,
    counterName text,
    FOREIGN KEY(counterName) REFERENCES counter (name))""")
    db.commit()

def add_counter(db, name, description):
    cursor = db.cursor()
    cursor.execute("""INSERT INTO counter VALUES (?, ?)""", (name, description))
    db.commit()

def increment_counter(db, name, event_date=None):
    cursor = db.cursor()
    if not event_date:
        from datetime import date
        event_date = date.today()
    cursor.execute("""INSERT INTO tracker VALUES (?, ?)""", (event_date, name))
    db.commit()

def get_counter_data(db, name):
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM counter WHERE name = ?""", (name,))
    return cursor.fetchall()

