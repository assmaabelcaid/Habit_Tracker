from db import get_db
from counter import Counter
from datetime import datetime


def preload_db():
    """
    Preload the database with predefined habits and their respective increment dates.
    gatito >=^v^=<
    """
    db = get_db()
    cursor = db.cursor()

    # Create tables if they do not exist
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

    # Predefined habits and their respective dates
    habits = {
        "water the plants": ["2025-04-01", "2025-04-02", "2025-04-03", "2025-04-04", "2025-04-05", "2025-04-06", "2025-04-07",
                  "2025-04-08", "2025-04-09", "2025-04-10", "2025-04-11", "2025-04-12", "2025-04-13", "2025-04-14",
                  "2025-04-15", "2025-04-16", "2025-04-17", "2025-04-18", "2025-04-19", "2025-04-20", "2025-04-21"
                  ],
        "pray": ["2025-04-01", "2025-04-02", "2025-04-03", "2025-04-04", "2025-04-05", "2025-04-06", "2025-04-07",
                  "2025-04-08", "2025-04-09", "2025-04-10", "2025-04-11", "2025-04-12", "2025-04-13", "2025-04-14",
                  "2025-04-15", "2025-04-16", "2025-04-17", "2025-04-18", "2025-04-19", "2025-04-20", "2025-04-21"],
        "clean the kitchen stove": ["2025-04-08", "2025-04-09", "2025-04-10", "2025-04-11", "2025-04-12", "2025-04-13", "2025-04-14",
                  "2025-04-15", "2025-04-16"],
        "exercise": ["2025-04-15", "2025-04-16", "2025-04-17", "2025-04-18"],
        "do the laundry": ["2025-04-22", "2025-04-23"],
        "MOURN THE DEATH OF THE POPE":["2025-04-21","2025-04-22","2025-04-23"]
    }

    for habit, dates in habits.items():
        cursor.execute('SELECT id FROM habits WHERE name = ?', (habit,))
        habit_id = cursor.fetchone()
        if not habit_id:
            counter = Counter(habit, f"{habit} habit", "Daily" if habit != "do the laundry" else "Weekly")
            counter.store(db)
            cursor.execute('SELECT id FROM habits WHERE name = ?', (habit,))
            habit_id = cursor.fetchone()[0]
        else:
            habit_id = habit_id[0]

        for date in dates:
            current_time = datetime.strptime(date, "%Y-%m-%d")
            cursor.execute('''INSERT INTO counters (habit_id, incremented_date)
                              VALUES (?, ?)''', (habit_id, current_time.strftime("%Y-%m-%d %H:%M:%S")))
            db.commit()


preload_db()