# Python & Web To-Do List

A beginner-friendly **To-Do List application available in both Python and Web versions**. The project is designed to help users manage daily tasks, organize priorities, track progress, and improve productivity through a simple and easy-to-use task-management system.

The project originally started as a basic Python command-line application and has gradually been improved with additional task-management features. A **web version** was later added to provide a more modern, visual, and student-friendly experience.

This project is part of my learning journey as an **Information Technology student**, where I am practicing programming, web development, problem solving, application design, and GitHub project management.

---

# Features

The project contains two versions:

* **Python Version** — Command-line task management application
* **Web Version** — Modern browser-based task management application

Both versions are designed around the same main purpose: helping users organize and manage their tasks.

---

# Python Version

The Python version is a command-line To-Do List application built using Python's standard library.

## Task Management

* Add new tasks
* View all tasks
* Mark tasks as completed
* Mark tasks as pending
* Delete individual tasks
* Edit existing tasks
* Clear all tasks
* Track task status
* Prevent empty tasks from being added

## Task Organization

Tasks can contain information such as:

* Task name
* Description
* Priority
* Category
* Due date
* Completion status

## Priority Levels

Tasks can be organized using:

```text
HIGH
MEDIUM
LOW
```

This helps users identify which tasks should be completed first.

## Categories

Tasks can be organized into categories such as:

```text
School
Work
Personal
Projects
Other
```

## Search and Filtering

Users can search for specific tasks instead of manually looking through the entire task list.

Tasks can also be filtered by:

* Completed
* Pending
* Priority
* Category

## Persistent Storage

The Python version can save tasks locally so that information can be loaded again when the application is restarted.

Depending on the implementation, tasks may be stored in:

```text
tasks.txt
```

## Input Validation

The application includes validation for common input errors, including:

* Empty task names
* Invalid task numbers
* Invalid menu choices
* Invalid priority selections
* Invalid date input

## Error Handling

Python exception handling is used to make the application safer when users enter invalid information.

Example:

```python
try:
    choice = int(input("Choose an option: "))
except ValueError:
    print("Please enter a valid number.")
```

---

# Web Version

The web version transforms the original command-line To-Do List into a more modern and visual browser-based application.

It was created to make the project easier to use while also giving me experience with **HTML, CSS, and JavaScript**.

The web version focuses on a clean, aesthetically pleasing, and student-friendly interface.

## Web Application Features

The web version is designed around common task-management functionality, including:

* Add tasks
* View tasks
* Complete tasks
* Edit tasks
* Delete tasks
* Task status tracking
* Task organization
* Priority management
* Categories
* Due dates
* Search and filtering
* Interactive task controls
* Responsive interface
* Modern visual design

## Student-Friendly Design

The web version was designed with students in mind.

The interface focuses on:

* Simple navigation
* Easy-to-read task information
* Clear task status
* Organized task sections
* Quick access to task actions
* Clean visual presentation
* Comfortable use on different screen sizes

The goal is to make the application feel more like a practical productivity tool rather than just a programming exercise.

---

# Web Technologies

The web version uses:

* **HTML5** — Page structure
* **CSS3** — Styling and responsive design
* **JavaScript** — Application logic and interactive features

No framework is required for the basic web version.

The project is designed so that the web application can be opened directly in a modern browser.

---

# Project Structure

```text
to-do-list/
│
├── python-version/
│   ├── main.py
│   └── tasks.txt
│
├── web-version/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── LICENSE
└── README.md
```

### File Description

| File         | Description                                  |
| ------------ | -------------------------------------------- |
| `main.py`    | Main Python To-Do List application           |
| `tasks.txt`  | Local task storage for the Python version    |
| `index.html` | Main webpage for the web version             |
| `style.css`  | Styling and layout for the web version       |
| `script.js`  | JavaScript functionality for the web version |
| `README.md`  | Project documentation                        |
| `LICENSE`    | Project license                              |

> The exact file names may change as the project continues to be developed.

---

# How the Python Version Works

When the Python application starts, users are presented with a menu containing the available task-management options.

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

Users can create a new task by selecting **Add Task**.

The application can collect:

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

---

# Completing a Task

When a task is finished, users can mark it as completed.

```text
Enter task number: 2

Task marked as completed!
```

The task will then display:

```text
[✓] Study Programming Concepts
```

The task remains in the list while its completion status changes.

---

# Editing a Task

Users can modify an existing task.

Possible information to change includes:

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

Users can remove individual tasks.

```text
Enter task number to delete: 3

Task deleted successfully!
```

---

# Searching Tasks

The search feature allows users to quickly find tasks.

Example:

```text
Enter task to search: Python

Search Results:

1. [ ] Finish Python assignment
2. [✓] Study Python
```

---

# Filtering Tasks

Tasks can be filtered according to different conditions.

Example:

```text
1. Show All
2. Show Pending
3. Show Completed
4. Show High Priority
5. Show School Tasks
```

For example:

```text
Filter: Pending

Pending Tasks:

1. [ ] Finish Python assignment
2. [ ] Create GitHub README
```

---

# Saving Tasks

Tasks can be saved locally.

```text
Saving tasks...

Tasks saved successfully!
```

This allows task information to be restored later.

---

# Loading Tasks

When the Python application starts, previously saved tasks can be loaded.

```text
Loading saved tasks...

Tasks loaded successfully!
```

This provides basic persistent storage without requiring a database.

---

# Web Version Usage

The web version is designed to run directly in a modern web browser.

## Option 1 — Open Directly

Navigate to the:

```text
web-version/
```

folder and open:

```text
index.html
```

The application should open in your default browser.

## Option 2 — Use VS Code

Open the project in **Visual Studio Code**.

Navigate to:

```text
web-version/index.html
```

Then open the HTML file in a browser.

If using a local development extension such as Live Server, the webpage can also be launched through the local development server.

---

# Requirements

## Python Version

* Python 3.x
* Git — optional

The Python version uses Python's standard library for its basic functionality.

No external packages are required for the command-line version unless additional features are introduced later.

## Web Version

* Modern web browser
* HTML5 support
* CSS3 support
* JavaScript support

No Python installation is required to use the basic web version.

---

# Development History

This project was developed progressively as a learning project.

## Version 1.0 — Basic Python To-Do List

The first version focused on basic task management.

### Included

* Add tasks
* View tasks
* Complete tasks
* Delete tasks
* Clear tasks
* Basic menu system

---

## Version 2.0 — Improved Python To-Do List

The Python application was expanded with additional task-management functionality.

### Added

* Task priorities
* Task categories
* Task descriptions
* Due dates
* Edit tasks
* Search tasks
* Filter tasks
* Persistent storage
* Input validation
* Error handling
* Improved task organization

---

## Version 3.0 — Web Version

The project was expanded from a command-line application into a browser-based application.

### Added

* HTML interface
* CSS styling
* JavaScript functionality
* Modern visual interface
* Student-friendly design
* Interactive task management
* Browser-based task organization
* Responsive layout
* Improved user experience

The web version represents the next stage of the project by applying programming concepts to frontend web development.

---

# Learning Objectives

This project helps develop practical programming and web-development skills.

## Python Fundamentals

The Python version practices:

* Variables
* Strings
* Integers
* Booleans
* Lists
* Dictionaries
* Functions
* Loops
* Conditional statements

## Programming Logic

The project demonstrates:

* `if`
* `elif`
* `else`
* `for` loops
* `while` loops
* Functions
* Conditions
* Menu-based program logic

## User Input

The Python application demonstrates how to:

* Receive user input
* Validate input
* Convert input types
* Handle invalid input
* Create interactive command-line programs

## Data Management

The project practices:

* Adding data
* Updating data
* Removing data
* Searching data
* Filtering data
* Tracking task status
* Organizing information

## File Handling

The Python version demonstrates:

* Creating files
* Reading files
* Writing files
* Saving application data
* Loading saved data

## Web Development

The web version introduces:

* HTML structure
* CSS styling
* JavaScript programming
* DOM manipulation
* Interactive webpage elements
* Responsive design
* Frontend application development
* User interface design

## Error Handling

The Python version introduces exception handling to prevent unexpected crashes caused by invalid user input.

---

# GitHub Learning

This project is also part of my learning journey with **Git and GitHub**.

Skills practiced include:

* Creating repositories
* Creating README files
* Organizing project files
* Creating project folders
* Committing changes
* Writing commit messages
* Pushing code to GitHub
* Updating existing projects
* Versioning projects
* Documenting software projects

---

# Project Goals

The main goal of this project is to continuously improve my programming and application-development skills.

Through this project, I am practicing how to:

1. Build an application from scratch
2. Plan application functionality
3. Organize project files
4. Write Python code
5. Write HTML and CSS
6. Use JavaScript
7. Create reusable functions
8. Work with data
9. Handle user input
10. Validate information
11. Implement application logic
12. Create interactive web applications
13. Debug applications
14. Use Git and GitHub
15. Document software projects
16. Improve an application through multiple versions

---

# Educational Purpose

This project was created primarily for **learning and practice**.

It demonstrates how a beginner programming project can gradually develop into a more complete application.

The project began as a simple Python command-line To-Do List and was later expanded into a web-based application. This progression allows me to practice both **Python programming and frontend web development** while learning how software projects can evolve over time.

As I continue studying Information Technology, more features and improvements may be added.

---

# Future Improvements

Possible future features include:

* [ ] Task reminders
* [ ] Automatic overdue detection
* [ ] Recurring tasks
* [ ] Advanced task sorting
* [ ] Advanced filtering
* [ ] Task statistics
* [ ] Productivity tracking
* [ ] Daily summaries
* [ ] Weekly summaries
* [ ] Calendar integration
* [ ] SQLite database
* [ ] JSON-based storage
* [ ] User accounts
* [ ] Login system
* [ ] Desktop application
* [ ] Mobile version
* [ ] Cloud synchronization
* [ ] Backend integration
* [ ] Online database
* [ ] User authentication
* [ ] Cross-device synchronization

---

# Project Status

**Current Status: Active Development**

The project is continuously being improved as I learn new programming and web-development concepts.

Current versions include:

| Version        | Status                | Description                   |
| -------------- | --------------------- | ----------------------------- |
| Python Version | Completed / Improving | Command-line task management  |
| Web Version    | Active Development    | Browser-based task management |

---

# Author

**Jose Navoa**

Student Developer

This project is part of my learning journey in:

* Information Technology
* Python Programming
* Web Development
* HTML
* CSS
* JavaScript
* Software Development
* Problem Solving
* Git and GitHub
* Application Development

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

# Acknowledgments

This project was created as a beginner-to-intermediate programming project.

It started as a simple Python command-line To-Do List and has gradually evolved into a project containing both a **Python application and a web application**.

The project reflects my progress as an Information Technology student and my continued learning in **Python, web development, software development, problem solving, and GitHub**.

More features and improvements may be added as I continue learning and developing my programming skills.
