from file_handler import load_data


TASK_FILE = "tasks.json"
STUDY_FILE = "study_records.json"


def show_statistics():
    """Display task and study statistics."""
    tasks = load_data(TASK_FILE)
    records = load_data(STUDY_FILE)

    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["completed"])
    pending_tasks = total_tasks - completed_tasks

    total_study_hours = sum(record["hours"] for record in records)

    print("\n--- Study Statistics ---")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Total study hours: {total_study_hours:.2f}")

    if records:
        subjects = {}

        for record in records:
            subject = record["subject"]
            subjects[subject] = subjects.get(subject, 0) + record["hours"]

        print("\nStudy hours by subject:")

        for subject, hours in subjects.items():
            print(f"- {subject}: {hours:.2f} hours")
    else:
        print("\nNo study records available.")