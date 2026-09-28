from file_handler import load_data, save_data


TASK_FILE = "tasks.json"


def add_task():
    """Add a new task."""
    title = input("Enter task title: ").strip()

    if not title:
        print("Task title cannot be empty.")
        return

    description = input("Enter task description: ").strip()

    task = {
        "title": title,
        "description": description,
        "completed": False
    }

    tasks = load_data(TASK_FILE)
    tasks.append(task)

    if save_data(TASK_FILE, tasks):
        print("Task added successfully.")
    else:
        print("Unable to save task.")


def view_tasks():
    """Display all tasks."""
    tasks = load_data(TASK_FILE)

    if not tasks:
        print("No tasks found.")
        return

    print("\n--- Your Tasks ---")

    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"

        print(f"{index}. {task['title']}")
        print(f"   Description: {task['description']}")
        print(f"   Status: {status}")


def complete_task():
    """Mark a task as completed."""
    tasks = load_data(TASK_FILE)

    if not tasks:
        print("No tasks found.")
        return

    view_tasks()

    try:
        number = int(input("Enter task number to complete: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return

        tasks[number - 1]["completed"] = True

        if save_data(TASK_FILE, tasks):
            print("Task marked as completed.")
        else:
            print("Unable to save changes.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    """Delete a task."""
    tasks = load_data(TASK_FILE)

    if not tasks:
        print("No tasks found.")
        return

    view_tasks()

    try:
        number = int(input("Enter task number to delete: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return

        deleted_task = tasks.pop(number - 1)

        if save_data(TASK_FILE, tasks):
            print(f"Task '{deleted_task['title']}' deleted successfully.")
        else:
            print("Unable to save changes.")

    except ValueError:
        print("Please enter a valid number.")