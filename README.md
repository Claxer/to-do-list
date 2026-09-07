# Python To-Do List

A beginner-friendly **To-Do List application built with Python** for managing daily tasks, tracking progress, organizing priorities, and keeping tasks saved between sessions.

This project started as a simple command-line To-Do List and has been improved with additional task-management features, better organization, input validation, persistent task storage, and more advanced application logic.

The project is designed as a practical way to practice **Python programming, functions, lists, dictionaries, loops, conditional statements, file handling, error handling, and application development**.

---

## Features

### Task Management

* Add new tasks
* View all tasks
* Mark tasks as completed
* Mark tasks as pending
* Delete individual tasks
* Edit existing tasks
* Clear all tasks
* Track task status
* Prevent empty tasks from being added

### Task Organization

* Task priorities
* Task categories
* Task descriptions
* Due dates
* Organized task information
* Completed and pending task tracking
* Search and filtering capabilities

### Task Status

Tasks can have different states depending on their progress.

Example:

```text
[ ] Pending
[✓] Completed
```

This makes it easier to see which tasks still need to be completed.

### Priority Levels

Tasks can be assigned different priority levels.

Example:

```text
HIGH
MEDIUM
LOW
```

This helps users focus on the most important tasks first.

### Categories

Tasks can be organized into categories such as:

```text
School
Work
Personal
Projects
Other
```

Categories make it easier to organize larger task lists.

### Persistent Storage

The application can save tasks to a local file.

This means tasks are not necessarily lost when the program is closed.

When the application starts again, previously saved tasks can be loaded.

### Search and Filtering

Users can search for specific tasks instead of manually checking the entire task list.

Tasks can also be filtered based on information such as:

* Completed
* Pending
* Priority
* Category

### Input Validation

The application includes input validation to prevent common errors.

For example:

* Empty task names
* Invalid task numbers
* Invalid menu choices
* Invalid priority selections
* Invalid date input

This helps prevent the application from crashing because of incorrect user input.

### Error Handling

The program uses Python error-handling techniques such as:

```python
try:
    ...
except ValueError:
    ...
```

This allows the application to handle invalid input more safely.

---

# Technologies Used

* **Python 3**
* Python Standard Library
* Lists
* Dictionaries
* Functions
* Loops
* Conditional Statements
* File Handling
* Exception Handling
* String Manipulation

No external Python packages are required for the basic version.

---

# Project Structure

```text
to-do-list/
│
├──python-version
   ├── main.py
   └── tasks.txt
├── LICENSE
└── README.md
```

Depending on the current version of the project, additional files may be included.

### File Description

| File        | Description                                               |
| ----------- | --------------------------------------------------------- |
| `main.py`   | Main Python application                                   |
| `tasks.txt` | Local task storage file, if persistent storage is enabled |
| `README.md` | Project documentation                                     |

> The exact file names may vary depending on the version of the project.

---

# How the Application Works

When the application starts, users are presented with a menu containing the available task-management options.

Example:

```text
=================================
          PYTHON TO-DO LIST
=================================

1. Add Task
2. View Tasks
3. Complete Task
4. Edit Task
5. Delete Task
6. Search Tasks
7. Filter Tasks
8. Clear Tasks
9. Save Tasks
10. Exit

Choose an option:
```

The user selects an option by entering its corresponding number.

---

# Adding a Task

Users can create a new task by selecting the **Add Task** option.

The application can collect information such as:

* Task name
* Description
* Priority
* Category
* Due date

Example:

```text
Enter task: Finish Python assignment
Enter description: Complete the programming activity
Enter priority: High
Enter category: School
Enter due date: 2026-09-10

Task added successfully!
```

---

# Viewing Tasks

The application displays the tasks currently stored in the system.

Example:

```text
=================================
             YOUR TASKS
=================================

1. [ ] Finish Python assignment
   Priority: HIGH
   Category: School
   Due: 2026-09-10

2. [✓] Study Programming Concepts
   Priority: MEDIUM
   Category: School
   Due: 2026-09-08

3. [ ] Create GitHub README
   Priority: LOW
   Category: Projects
   Due: 2026-09-12
```

This provides a quick overview of the user's current tasks.

---

# Completing a Task

When a task is finished, users can mark it as completed.

Example:

```text
Enter task number: 2

Task marked as completed!
```

The task will then appear as:

```text
[✓] Study Programming Concepts
```

The application keeps the task in the list while changing its completion status.

---

# Editing a Task

Users can modify an existing task if information needs to be changed.

For example, a user may want to change:

* Task name
* Description
* Priority
* Category
* Due date

Example:

```text
Enter task number to edit: 1

Enter new task name:
Finish Python project

Task updated successfully!
```

---

# Deleting a Task

Users can remove individual tasks that are no longer needed.

Example:

```text
Enter task number to delete: 3

Task deleted successfully!
```

The selected task is removed from the task list.

---

# Searching Tasks

The search feature allows users to find a specific task quickly.

Example:

```text
Enter task to search: Python

Search Results:

1. [ ] Finish Python assignment
2. [✓] Study Python
```

This is useful when the application contains many tasks.

---

# Filtering Tasks

Users can filter their task list based on different conditions.

Examples include:

```text
1. Show All
2. Show Pending
3. Show Completed
4. Show High Priority
5. Show School Tasks
```

Example:

```text
Filter: Pending

Pending Tasks:

1. [ ] Finish Python assignment
2. [ ] Create GitHub README
```

---

# Clearing Tasks

The application can remove all stored tasks.

Because this action can remove multiple tasks at once, the program can ask the user for confirmation.

Example:

```text
Are you sure you want to clear all tasks? (y/n): y

All tasks have been cleared.
```

---

# Saving Tasks

Tasks can be saved locally so they can be restored later.

Example:

```text
Saving tasks...

Tasks saved successfully!
```

Depending on the implementation, task information may be stored in a local text file.

Example:

```text
tasks.txt
```

---

# Loading Tasks

When the application starts, previously saved tasks can be loaded from the local storage file.

Example:

```text
Loading saved tasks...

Tasks loaded successfully!
```

This provides basic persistent data storage without requiring a database.

---

# Example Usage

A typical session may look like this:

```text
=================================
          PYTHON TO-DO LIST
=================================

1. Add Task
2. View Tasks
3. Complete Task
4. Edit Task
5. Delete Task
6. Search Tasks
7. Filter Tasks
8. Clear Tasks
9. Save Tasks
10. Exit

Choose an option: 1
```

The user adds a task:

```text
Enter task: Study Python

Enter priority: High

Enter category: School

Task added successfully!
```

Viewing the task:

```text
YOUR TASKS

1. [ ] Study Python
   Priority: HIGH
   Category: School
```

After completing the task:

```text
1. [✓] Study Python
   Priority: HIGH
   Category: School
```

---

# Learning Objectives

This project is designed to help develop practical Python programming skills.

## Python Fundamentals

The project practices:

* Variables
* Strings
* Integers
* Booleans
* Lists
* Dictionaries
* Functions

## Programming Logic

The application uses:

* `if`
* `elif`
* `else`
* `for` loops
* `while` loops
* Functions
* Conditions
* Menu-based program logic

## User Input

The project demonstrates how to:

* Receive user input
* Validate input
* Convert input types
* Handle invalid input
* Create interactive command-line programs

## Data Management

The application practices:

* Adding data
* Updating data
* Removing data
* Searching data
* Filtering data
* Tracking task status
* Organizing information

## File Handling

The project demonstrates basic file operations such as:

* Creating files
* Reading files
* Writing files
* Saving application data
* Loading saved data

## Error Handling

The project also introduces exception handling to prevent unexpected program crashes.

Example:

```python
try:
    choice = int(input("Choose an option: "))
except ValueError:
    print("Please enter a valid number.")
```

---

# Installation

## 1. Install Python

Make sure Python 3 is installed on your computer.

Check your Python version using:

```bash
python --version
```

On Windows, you can also use:

```bash
py --version
```

---

## 2. Clone the Repository

Clone the repository using Git:

```bash
git clone https://github.com/YOUR-USERNAME/python-to-do-list.git
```

Replace:

```text
YOUR-USERNAME
```

with your GitHub username.

Then enter the project folder:

```bash
cd python-to-do-list
```

---

## 3. Run the Application

Run the main Python file:

```bash
python main.py
```

On Windows, you can also use:

```bash
py main.py
```

---

# Requirements

* Python 3.x
* Git — optional, only required if cloning the repository

The current command-line version is designed to use Python's standard library.

No external packages are required unless additional features are added in future versions.

---

# Project Development

This project was developed progressively as a learning project.

### Initial Version

The first version focused on basic task management:

* Add tasks
* View tasks
* Complete tasks
* Delete tasks
* Clear tasks

### Improved Version

The improved version expands the application with more practical functionality, including:

* Task priorities
* Task categories
* Task descriptions
* Due dates
* Editing tasks
* Searching tasks
* Filtering tasks
* Persistent task storage
* Improved input validation
* Error handling
* Better task organization
* More structured application logic

The goal is to gradually transform a simple Python exercise into a more complete task-management application.

---

# Future Improvements

There are still many ways this project can be improved.

Possible future features include:

* [ ] Task reminders
* [ ] Automatic overdue detection
* [ ] Recurring tasks
* [ ] Task sorting
* [ ] Advanced filtering
* [ ] Task statistics
* [ ] Productivity tracking
* [ ] Daily task summaries
* [ ] Weekly task summaries
* [ ] Calendar integration
* [ ] SQLite database
* [ ] JSON-based storage
* [ ] User accounts
* [ ] Login system
* [ ] Graphical user interface
* [ ] Dark mode
* [ ] Desktop application
* [ ] Web version
* [ ] Mobile version
* [ ] Cloud synchronization

---

# Version History

## Version 1.0 — Basic To-Do List

The initial version introduced the core task-management functionality.

### Included

* Add tasks
* View tasks
* Complete tasks
* Delete tasks
* Clear tasks
* Basic menu system

---

## Version 2.0 — Improved To-Do List

The application was expanded with more advanced task-management features.

### Added

* Task priorities
* Task categories
* Task descriptions
* Due dates
* Edit tasks
* Search tasks
* Filter tasks
* Persistent storage
* Improved validation
* Error handling
* Improved task organization

---

# Project Goals

The main goal of this project is to build a practical Python application while continuously improving programming skills.

Through this project, I am practicing how to:

1. Build an application from scratch
2. Plan program functionality
3. Organize Python code
4. Create reusable functions
5. Work with lists and dictionaries
6. Handle user input
7. Validate user input
8. Implement application logic
9. Manage and update data
10. Work with files
11. Handle programming errors
12. Debug Python applications
13. Use Git and GitHub
14. Document a software project
15. Improve an application through multiple versions

---

# GitHub Learning

This project is also part of my learning journey with **Git and GitHub**.

Some of the skills practiced through this project include:

* Creating repositories
* Creating README files
* Organizing project files
* Committing changes
* Writing commit messages
* Pushing code to GitHub
* Updating existing projects
* Versioning projects
* Documenting applications

---

# Educational Purpose

This project was created primarily for **learning and practice**.

It demonstrates how a beginner Python project can gradually become more structured and feature-rich as programming knowledge improves.

The project may continue to change as new Python concepts are learned and implemented.

---

# License

This project is intended for **educational and personal use**.

You are welcome to:

* Study the code
* Modify the code
* Experiment with new features
* Use the project as a learning reference
* Improve the application

---

# Author

**Jose Navoa**

Student Developer

This project is part of my journey in learning:

* Information Technology
* Python Programming
* Software Development
* Problem Solving
* Git and GitHub
* Application Development

---

# Acknowledgments

This project was created as a beginner-to-intermediate Python programming project.

It started as a simple command-line To-Do List and has been continuously improved to practice more advanced programming concepts and real-world application development.

More features and improvements may be added as I continue learning **Python, software development, and Information Technology**.
