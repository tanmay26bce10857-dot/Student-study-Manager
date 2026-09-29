from file_handler import load, save

file = "study_records.json"

def add_study_record():
    subject = input("Enter subject name: ").strip()

    if not subject:
        print("Subject name cannot be empty.")
        return

    try:
        hours = float(input("Enter study hours: "))

        if hours <= 0:
            print("Study hours must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    topic = input("Enter topic studied: ").strip()

    record = {
        "subject": subject,
        "hours": hours,
        "topic": topic
    }

    records = load(file)
    records.append(record)

    if save(file, records):
        print("Study record added successfully.")
    else:
        print("Unable to save study record.")

def view_study_records():
    records = load(file)

    if not records:
        print("No study records found.")
        return

    print("\n--- Study Records ---")

    for i, record in enumerate(records, 1):
        print(f"{i}. Subject: {record['subject']}")
        print(f"   Hours: {record['hours']}")
        print(f"   Topic: {record['topic']}")