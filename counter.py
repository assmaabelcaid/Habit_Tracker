from db import add_counter, increment_counter

class Counter:
    def __init__(self, name: str, description: str):
        """
        Counter class to count events
        :param name: the name of the counter
        :param description: the description of the counter
        """
        self.name = name
        self.description = description
        self.count = 0

    def increment(self):
        self.count += 1

    def __str__(self):
        return f'{self.name}: {self.count}'

    def reset(self):
        self.count = 0

    def store(self, db):
        add_counter(db, self.name, self.description)

    def add_event(self, db, date: str = None):
        increment_counter(db, self.name, date)


