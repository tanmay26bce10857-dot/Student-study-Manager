# Student Study & Task Management System

## 1. Project Overview

The Student Study & Task Management System is a Python-based console application designed to help students manage their daily tasks and study activities.

The system allows users to create and manage tasks, record study sessions, and view basic productivity statistics.

## 2. Features

### Task Management
- Add new tasks
- View all tasks
- Mark tasks as completed
- Delete tasks

### Study Management
- Add study records
- Record subject, study hours, and topic
- View study records

### Statistics
- View total number of tasks
- View completed and pending tasks
- View total study hours
- View study hours by subject

### Data Storage
- Data is stored locally using JSON files.
- The application automatically creates the required data folder.

## 3. Technologies Used

- Python 3
- JSON
- Python Standard Library
- Git and GitHub
- Visual Studio Code

## 4. Project Structure

```text
Student-study-manager/
│
├── data/
│   ├── tasks.json
│   └── study_records.json
│
├── tests/
│   └── test_project.py
│
├── main.py
├── task_manager.py
├── study_manager.py
├── statistics.py
├── file_handler.py
├── statement.md
├── README.md
└── .gitignore
