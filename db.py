import sqlite3
from counter import Counter


def get_db():
    """
        Initializes and returns the connection of the database.
        gatito >=^v^=<.
    """
    db = sqlite3.connect('main.db')
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS habits (
                        id INTEGER PRIMARY KEY,
                        name TEXT UNIQUE NOT NULL,
                        description TEXT,
                        period TEXT NOT NULL,
                        creation_date TEXT
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS counters (
                        id INTEGER PRIMARY KEY,
                        habit_id INTEGER,
                        incremented_date TEXT,
                        FOREIGN KEY (habit_id) REFERENCES habits (id)
                    )''')
    db.commit()
    return db


def get_habits_name(db): # this function retrieves all habits from the database
    cursor = db.cursor()
    cursor.execute('SELECT name FROM habits')
    rows = cursor.fetchall()
    return [row[0] for row in rows]


def habit_by_period(db, period): # this function retrieves the habit names filtered by their period
    cursor = db.cursor()
    cursor.execute('SELECT name FROM habits WHERE period = ?', (period,))
    rows = cursor.fetchall()
    return [row[0] for row in rows]


def get_counter(db, name): # this function retrieves the counter object for a given habit name
    cursor = db.cursor()
    cursor.execute('SELECT * FROM habits WHERE name = ?', (name,))
    habit = cursor.fetchone()
    if habit:
        return Counter(habit[1], habit[2], habit[3], habit[0])
    else:
        return None