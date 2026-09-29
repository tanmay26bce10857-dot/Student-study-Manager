from file_handler import load

task_file = "tasks.json"
study_file = "study_records.json"

def show_statistics():
    tasks = load(task_file)
    records = load(study_file)

    total = len(tasks)
    done = sum(1 for task in tasks if task["completed"])
    pending = total - done

    hours = sum(record["hours"] for record in records)

    print("\n--- Study Statistics ---")
    print(f"Total tasks: {total}")
    print(f"Completed tasks: {done}")
    print(f"Pending tasks: {pending}")
    print(f"Total study hours: {hours:.2f}")

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