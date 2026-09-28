from task_manager import add_task, view_tasks, complete_task, delete_task
from study_manager import add_study_record, view_study_records
from statistics import show_statistics


def task_menu():
    while True:
        print("\n--- Task Management ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


def study_menu():
    while True:
        print("\n--- Study Management ---")
        print("1. Add Study Record")
        print("2. View Study Records")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_study_record()
        elif choice == "2":
            view_study_records()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


def main():
    while True:
        print("\n================================")
        print(" STUDENT STUDY & TASK MANAGER")
        print("================================")
        print("1. Task Management")
        print("2. Study Management")
        print("3. View Statistics")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            task_menu()
        elif choice == "2":
            study_menu()
        elif choice == "3":
            show_statistics()
        elif choice == "4":
            print("Thank you for using Student Study & Task Manager.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
    
    