# Habit Tracker

Introducing a Habit Tracking App project, because it's slay.
 

## What is it?

This App was programmed with Python. It's a simple Command Line Interface (CLI) App designed to track your habits. 
You can intuitively create, complete, update, delete, and monitor your tasks with ease. 

## How to install it?

1. Download the repository from GitHub: https://github.com/assmaabelcaid/Habit_Tracker
2. Make sure you have Python 3.11+ installed on your computer.
3. Run the command to install the required libraries:


```shell
pip install -r requirements.txt
```


## Load the database:

In order to give you a test case where you can analyse pre-existing habits, run:

```shell
python preload.py
```

## How it works:

1. Run `python main.py` to start the App.


### Creating a New Habit

* Run the application and select "Create a New Habit".
* Enter the name of your new habit.
* Enter a description for your habit.
* Choose whether it's a Daily or Weekly habit.
* The habit will be created and stored in the database.

### Completing a Task

* Run the application and select "Increment Habit".
* Select the habit you want to increment.
* The habit's count will be incremented by 1, and the last increment date will be updated.

### Resetting a Habit

* Run the application and select "Reset Habit".
* Select the habit you want to reset.
* The habit's count will be reset to 0.

### Analyzing Habits

1. Run the application and select "Analyse Habits".
2. Choose from the following options:

* List all habits: View a list of all currently tracked habits.
* List habits by periodicity: View habits filtered by their periodicity (Daily or Weekly).
* Longest streak of all habits: View the longest streak achieved among all habits.
* Longest streak for a habit: View the longest streak achieved for a specific habit.

### Deleting a Habit

1. Run the application and select "Delete Habit".
2. Select the habit you want to delete.
3. The habit will be removed from the database.

## Example Habits

This program comes with a test case of predefined habits that can be used for testing purpose:
### Daily:
* water the plants
* pray 
* clean the kitchen stove
* exercise
* MOURN THE DEATH OF THE POPE 
### Weekly:
* do the laundry



Note: It's giving purr <3.

## Tests:

1. Test this mada like no one else
```shell
pytest test_project.py
```
The `test_project.py` module is designed to automate testing of the habit tracking app's functionality, 
ensuring that the core features like creating, incrementing, resetting, and deleting habits work correctly, 
and that database operations are performed as expected.

Run the more detailed test using the following command:

```shell
pytest -v test_project.py
```
That's it! Hope you have fun!!

*Assmaa Belcaid*