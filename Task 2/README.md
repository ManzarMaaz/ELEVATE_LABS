# Task 2: Persistent Command-Line To-Do List Application ✅
This project is a simple, console-based To-Do List manager that uses Python lists to hold tasks and file handling to ensure task persistence between sessions.

## Deliverables
```
todo.py

tasks.txt (This file is generated automatically when you run the app.)
```
## Features
```
Persistence: Tasks are stored in a text file (tasks.txt) using file I/O, meaning the list is saved when the app closes and reloaded when it starts.

Functionality: Supports Add, View, and Remove tasks.

File Handling: Uses the with open() context manager for safe and efficient file reading/writing.

Data Structure: Tasks are managed using a Python list.

String Manipulation: Uses .strip() to clean up newline characters (’n’) from file reads.
```
## How to Run
```
Save the file: Ensure the file is saved as todo.py.

Open Terminal: Navigate to the directory where you saved the file.

Execute: Run the script using the Python interpreter:
```
```bash
python todo.py
Follow Prompts: Use options 1, 2, or 3 to manage your tasks. The tasks.txt file will be created/updated in the same directory.
```
## Key Concepts Utilized
```
File Handling: Using open() with ’r’ (read) and ’w’ (write) modes.

Context Managers (with statement): Ensuring files are closed properly.

Lists: The primary data structure for task management.

Functions: load_tasks, save_tasks, view_tasks, add_task, remove_task for modularity.

String Methods: Specifically .strip() for data cleaning.
```
