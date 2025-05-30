from db import get_habits_name
from datetime import datetime


# This function calculates the longest streak for the chosen habit
def calculate_longest_streak(db, habit_name):
    """
        Calculates the longest streak of a habit.

        Parameters:
        db : sqlite3.Connection (database connection)
        habit_name : str (The name of the habit)

        Returns:
        int: The longest streak of the habit.
        """
    cursor = db.cursor()
    cursor.execute('''SELECT incremented_date FROM counters
                      INNER JOIN habits ON counters.habit_id = habits.id 
                      WHERE habits.name = ?
                      ORDER BY incremented_date ASC''', (habit_name,))
    rows = cursor.fetchall()

    if not rows:
        return 0

    dates = [datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S") for row in rows]


    longest_streak = 1
    current_streak = 1

    for i in range(1, len(dates)):
        if (dates[i] - dates[i - 1]).days == 1:
            current_streak += 1
            print(f"Current streak incremented: {current_streak}")
        else:
            longest_streak = max(longest_streak, current_streak)
            print(f"New longest streak found: {longest_streak}")
            current_streak = 1

    longest_streak = max(longest_streak, current_streak)
    print(f"Final longest streak: {longest_streak}")
    return longest_streak


# This function calculates the longest streak from all habits
def longest_streak_all_habits(db):
    """
        Calculate the longest streak for all habits in the database.

        Parameters:
        db : sqlite3.Connection (The database connection)

        Returns:
        int: The longest streak among all habits.
        """
    habits = get_habits_name(db)
    longest_streak = 0
    for habit in habits:
        streak = calculate_longest_streak(db, habit)
        if streak > longest_streak:
            longest_streak = streak
    return longest_streak