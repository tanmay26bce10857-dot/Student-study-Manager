from file_handler import load, save

file = "tasks.json"

def add_task():
    title = input("Enter task title: ").strip()

    if not title:
        print("Task title cannot be empty.")
        return

    desc = input("Enter task description: ").strip()

    task = {
        "title": title,
        "description": desc,
        "completed": False
    }

    tasks = load(file)
    tasks.append(task)

    if save(file, tasks):
        print("Task added successfully.")
    else:
        print("Unable to save task.")

def view_tasks():
    tasks = load(file)

    if not tasks:
        print("No tasks found.")
        return

    print("\n--- Your Tasks ---")

    for i, task in enumerate(tasks, 1):
        status = "Completed" if task["completed"] else "Pending"

        print(f"{i}. {task['title']}")
        print(f"   Description: {task['description']}")
        print(f"   Status: {status}")

def complete_task():
    tasks = load(file)

    if not tasks:
        print("No tasks found.")
        return

    view_tasks()

    try:
        num = int(input("Enter task number to complete: "))

        if num < 1 or num > len(tasks):
            print("Invalid task number.")
            return

        tasks[num - 1]["completed"] = True

        if save(file, tasks):
            print("Task marked as completed.")
        else:
            print("Unable to save changes.")

    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    tasks = load(file)

    if not tasks:
        print("No tasks found.")
        return

    view_tasks()

    try:
        num = int(input("Enter task number to delete: "))

        if num < 1 or num > len(tasks):
            print("Invalid task number.")
            return

        deleted = tasks.pop(num - 1)

        if save(file, tasks):
            print(f"Task '{deleted['title']}' deleted successfully.")
        else:
            print("Unable to save changes.")

    except ValueError:
        print("Please enter a valid number.")