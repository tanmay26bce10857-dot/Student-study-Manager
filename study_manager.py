from file_handler import load_data, save_data


STUDY_FILE = "study_records.json"


def add_study_record():
    """Add a new study session."""
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

    records = load_data(STUDY_FILE)
    records.append(record)

    if save_data(STUDY_FILE, records):
        print("Study record added successfully.")
    else:
        print("Unable to save study record.")


def view_study_records():
    """Display all study records."""
    records = load_data(STUDY_FILE)

    if not records:
        print("No study records found.")
        return

    print("\n--- Study Records ---")

    for index, record in enumerate(records, start=1):
        print(f"{index}. Subject: {record['subject']}")
        print(f"   Hours: {record['hours']}")
        print(f"   Topic: {record['topic']}")