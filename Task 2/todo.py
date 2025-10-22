# Simple To-Do List App

tasks = []

def show_menu():
    print("\n------ TO-DO LIST MENU ------")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for _, task in enumerate(tasks, 1):
            print(f"{_}. {task}")

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("New Task added!")

def remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to remove: "))
        if 0 < task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Exiting To-Do List App.")
        break
    else:
        print("Invalid choice. Please select from 1 to 4.")
