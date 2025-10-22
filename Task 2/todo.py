TODO_FILE = "tasks.txt"

def load_tasks():
    try:
        with open(TODO_FILE, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def view_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty! ✅")
        return
    print("\n--- To-Do List ---")
    for index, task in enumerate(tasks, 1):
        print(f"{index}. {task}")
    print("------------------")

def add_task(tasks):
    task = input("Enter the new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"Task added: '{task}'")
    else:
        print("Task cannot be empty.")

def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("Enter the number of the task to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task removed: '{removed_task}'")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def todo_cli():
    tasks = load_tasks()
    print("Welcome to the To-Do List Manager!")

    while True:
        print("\nOptions:")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Saving tasks and exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    todo_cli()
