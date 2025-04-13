from datetime import datetime


class Counter:

    def __init__(self, name, description, period, id=None):
        """
        Constructs all the necessary attributes for the Counter object.

        Parameters:
        ----------
        name : str
            Name of the habit.
        description : str
            Description of the habit.
        periodicity : str
            Frequency of the habit (e.g., "Daily", "Weekly").
        id : int, optional
            Unique identifier for the habit (default is None).
        """
        self.id = id
        self.name = name
        self.description = description
        self.period = period
        self.creation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def store(self, db):
        """
        Stores the habit in the database.

        Parameters:
        ----------
        db : sqlite3.Connection
            The database connection.
        """
        cursor = db.cursor()
        cursor.execute('''INSERT INTO habits (name, description, period, creation_date)
                          VALUES (?, ?, ?, ?)''', (self.name, self.description, self.period, self.creation_date))
        db.commit()
        self.id = cursor.lastrowid

    def increment(self, db, incremented_date=None):
        """
        Increments the counter for the habit, optionally using a specified date.

        Parameters:
        ----------
        db : sqlite3.Connection
            The database connection.
        increment_date : datetime, optional
            The date to use for the increment (default is None, which uses the current date and time).
        """
        cursor = db.cursor()
        if incremented_date is None:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            current_time = incremented_date.strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute('''INSERT INTO counters (habit_id, incremented_date)
                          VALUES (?, ?)''', (self.id, current_time))
        db.commit()

    def reset(self, db):
        """
        Resets the counter for the habit by deleting all related entries in the counters table.

        Parameters:
        ----------
        db : sqlite3.Connection
            The database connection.
        """
        cursor = db.cursor()
        cursor.execute('''DELETE FROM counters WHERE habit_id = ?''', (self.id,))
        db.commit()

    def delete(self, db):
        """
        Deletes the habit and its counters from the database.

        Parameters:
        ----------
        db : sqlite3.Connection
            The database connection.
        """
        cursor = db.cursor()
        cursor.execute('''DELETE FROM habits WHERE id = ?''', (self.id,))
        cursor.execute('''DELETE FROM counters WHERE habit_id = ?''', (self.id,))
        db.commit()