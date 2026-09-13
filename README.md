# Python & Web To-Do List

A beginner-friendly **To-Do List application available in both Python and Web versions**. The project is designed to help users manage daily tasks, organize priorities, track progress, and improve productivity through a simple and easy-to-use task-management system.

The project originally started as a basic Python command-line application and has gradually been improved with additional task-management and productivity features. A **web version** was later added to provide a more modern, visual, and student-friendly experience.

The Python version now includes features such as **productivity dashboards, today's tasks, overdue tasks, upcoming tasks, task notes, focus tasks, productivity scores, weekly reports, task archiving, multiple-task completion, and a Pomodoro focus timer**.

This project is part of my learning journey as an **Information Technology student**, where I am practicing programming, web development, problem solving, application design, and GitHub project management.

---

# Features

The project contains two versions:

* **Python Version** — Command-line task management and productivity application
* **Web Version** — Modern browser-based task management application

Both versions are designed around the same main purpose: helping users organize and manage their tasks.

---

# Python Version

The Python version is a command-line To-Do List application built using Python's standard library.

It has developed from a simple task list into a more complete **personal productivity system**.

## Task Management

* Add new tasks
* View all tasks
* Mark tasks as completed
* Mark tasks as pending
* Delete individual tasks
* Edit existing tasks
* Duplicate existing tasks
* Clear completed tasks
* Delete all tasks with confirmation
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
* Creation date
* Notes
* Focus status

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

Users can also view a summary of how many tasks belong to each category.

---

# Productivity Features

The Python version now includes additional features designed to help users manage their workload and become more productive.

## Productivity Dashboard

The **Productivity Dashboard** provides a quick overview of the user's current tasks.

It displays information such as:

* Total tasks
* Completed tasks
* Pending tasks
* High-priority tasks
* Tasks due today
* Overdue tasks
* Completion rate
* Visual progress bar

Example:

```text
========== PRODUCTIVITY DASHBOARD ==========

Total Tasks:       15
Completed:         8
Pending:           7
High Priority:     3
Due Today:         2
Overdue:           1

Completion Rate: 53.3%

Progress:
[################--------------]
```

This gives users a quick way to understand their current workload without manually checking every task.

---

# Today's Tasks

The **Today's Tasks** feature shows pending tasks that are due on the current date.

Example:

```text
========== TODAY'S TASKS ==========

You have 2 task(s) due today.

ID: 4
Task: Finish Python Assignment
Priority: High
Category: School
Due Date: 2026-09-13
Status: Pending
```

This allows users to immediately focus on tasks that need attention today.

---

# Overdue Tasks

The application can identify tasks whose due dates have already passed.

The **Overdue Tasks** feature displays these tasks separately so users can quickly see unfinished work that needs attention.

Example:

```text
========== OVERDUE TASKS ==========

You have 2 overdue task(s).
```

This helps prevent important tasks from being forgotten.

---

# Upcoming Tasks

The **Upcoming Tasks** feature displays pending tasks that are due within the next seven days.

This helps users prepare for upcoming deadlines instead of only focusing on tasks that are due immediately.

Example:

```text
========== UPCOMING TASKS ==========

Finish database activity
Due Date: 2026-09-15

Prepare presentation
Due Date: 2026-09-17

Submit project
Due Date: 2026-09-19
```

---

# Task Notes

Users can attach additional notes to individual tasks.

This can be useful for:

* Assignment instructions
* Important reminders
* Small details
* Project requirements
* Ideas
* Additional information

Example:

```text
Task: Finish Python Assignment

Note:
Remember to include input validation.
```

Multiple notes can be stored for the same task.

---

# Focus Task

The **Focus Task** feature allows users to choose one task as their main priority.

Users can:

* Set a focus task
* View the current focus task
* Remove the focus task

This encourages users to concentrate on one important task instead of trying to work on everything at once.

---

# Productivity Score

The application includes a simple **Productivity Score** based on the percentage of tasks completed.

Example:

```text
========== PRODUCTIVITY SCORE ==========

Your productivity score is: 75.0%

Good job! You are making strong progress.
```

The application provides different messages depending on the user's completion percentage.

---

# Weekly Productivity Report

The **Weekly Productivity Report** provides a basic summary of activity during the current week.

It tracks information such as:

* Tasks created during the week
* Completed tasks
* Current pending tasks

Example:

```text
========== WEEKLY PRODUCTIVITY REPORT ==========

Week: 2026-09-07 to 2026-09-13

Tasks Created This Week: 8
Completed Tasks: 6
Current Pending Tasks: 5
```

This gives users a simple way to review their productivity.

---

# Category Summary

The **Category Summary** provides a breakdown of tasks by category.

For example:

```text
Category: School
Total: 8
Completed: 5
Pending: 3

Category: Personal
Total: 4
Completed: 3
Pending: 1

Category: Projects
Total: 5
Completed: 2
Pending: 3
```

This makes it easier to see which areas of life or work have the most unfinished tasks.

---

# Quick Complete

Users can complete multiple tasks at once by entering several task IDs.

Example:

```text
Enter task IDs separated by commas.

Example: 1, 3, 5

Task IDs: 1, 3, 5

3 task(s) completed.
```

This is useful when several related tasks have been completed and the user does not want to update them individually.

---

# Duplicate Tasks

The **Duplicate Task** feature allows users to quickly create a copy of an existing task.

For example:

```text
Original:
Study Python

Duplicated:
Study Python (Copy)
```

This can be useful for similar assignments, repeated project tasks, or tasks that share the same information.

---

# Task Archiving

Completed tasks can be moved into a separate archive instead of being permanently deleted.

Archived tasks are stored in:

```text
archived_tasks.json
```

Users can:

* Archive completed tasks
* View archived tasks
* Keep completed work separate from current tasks

This helps keep the main task list clean while preserving previous tasks.

---

# Pomodoro Focus Timer

The Python application now includes a basic **Pomodoro-style focus timer**.

Users can choose:

```text
1. 25 minute focus
2. 15 minute focus
3. Custom timer
```

The timer counts down while the user focuses on their work.

Example:

```text
Focus session started for 25 minute(s).

Time Remaining: 24:59
```

When the timer finishes:

```text
Focus session complete!
```

The timer can also be stopped manually using `Ctrl+C`.

This feature is intended to encourage focused work sessions while completing tasks.

---

# Search and Filtering

Users can search for specific tasks instead of manually looking through the entire task list.

Tasks can also be filtered by:

* Completed
* Pending
* High priority
* Medium priority
* Low priority
* Category

This makes it easier to find specific tasks in a larger task list.

---

# Sorting

The Python version can organize tasks using different sorting methods.

Available sorting options include:

* Priority
* Due date
* Name
* Status

This allows users to organize their task list based on what they need to focus on.

---

# Statistics

The application includes a statistics section that provides an overview of the user's tasks.

It can display:

* Total tasks
* Completed tasks
* Pending tasks
* High-priority tasks
* Medium-priority tasks
* Low-priority tasks
* Category breakdown

This provides a simple way to understand how tasks are distributed.

---

# Persistent Storage

The Python version can save tasks locally so that information can be loaded again when the application is restarted.

The current version uses:

```text
tasks.json
```

Completed tasks can also be archived separately using:

```text
archived_tasks.json
```

This provides persistent storage without requiring a database.

---

# Input Validation

The application includes validation for common input errors, including:

* Empty task names
* Invalid task numbers
* Invalid menu choices
* Invalid priority selections
* Invalid date input
* Invalid task IDs
* Invalid timer values

## Example

```python
try:
    choice = int(input("Choose an option: "))
except ValueError:
    print("Please enter a valid number.")
```

---

# Error Handling

Python exception handling is used to make the application safer when users enter invalid information.

The application also handles situations such as:

* Missing task files
* Corrupted JSON files
* Invalid dates
* Invalid task IDs
* Invalid numerical input

Example:

```python
try:
    with open(FILE_NAME, "r") as file:
        return json.load(file)

except FileNotFoundError:
    return []

except json.JSONDecodeError:
    print("Warning: Task file is corrupted.")
    return []
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
│   ├── tasks.json
│   └── archived_tasks.json
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

| File                  | Description                                         |
| --------------------- | --------------------------------------------------- |
| `main.py`             | Main Python To-Do List and productivity application |
| `tasks.json`          | Local task storage for the Python version           |
| `archived_tasks.json` | Storage for archived completed tasks                |
| `index.html`          | Main webpage for the web version                    |
| `style.css`           | Styling and layout for the web version              |
| `script.js`           | JavaScript functionality for the web version        |
| `README.md`           | Project documentation                               |
| `LICENSE`             | Project license                                     |

> The exact file names may change as the project continues to be developed.

---

# How the Python Version Works

When the Python application starts, users are presented with a menu containing the available task-management options.

Example:

```text
=============================================
                 TO-DO LIST
=============================================

1.  View All Tasks
2.  Add Task
3.  Edit Task
4.  Complete / Uncomplete Task
5.  Delete Task
6.  Search Tasks
7.  Filter Tasks
8.  Sort Tasks
9.  Task Statistics
10. Clear Completed Tasks
11. Productivity Center
12. Task Tools
13. Exit

Choose an option:
```

The main menu keeps the original task-management functions while grouping the newer productivity features into dedicated sections.

---

# Productivity Center

The **Productivity Center** contains features focused on helping users plan their workload and improve productivity.

```text
=============================================
          PRODUCTIVITY CENTER
=============================================

1. Dashboard
2. Today's Tasks
3. Overdue Tasks
4. Upcoming Tasks
5. Productivity Score
6. Weekly Report
7. Category Summary
8. Pomodoro Timer
9. Back
```

This keeps the main menu organized even as more features are added.

---

# Task Tools

The **Task Tools** section contains additional tools for managing individual tasks.

```text
=============================================
              TASK TOOLS
=============================================

1. Add Task Note
2. View Task Notes
3. Duplicate Task
4. Complete Multiple Tasks
5. Set Focus Task
6. View Focus Task
7. Remove Focus Task
8. Archive Completed Tasks
9. View Archived Tasks
10. Delete All Tasks
11. Back
```

This organization helps prevent the main menu from becoming too crowded.

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
Enter due date: 2026-09-15

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

ID: 1
Task: Finish Python assignment
Description: Complete the programming activity
Priority: High
Category: School
Due Date: 2026-09-15
Status: Pending
Created: 2026-09-13 09:00
```

---

# Completing a Task

When a task is finished, users can mark it as completed.

```text
Enter task ID: 2

Task marked as completed.
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

Users can leave a field blank to keep its existing value.

---

# Deleting a Task

Users can remove individual tasks.

The application asks for confirmation before permanently deleting the selected task.

```text
Task: Create GitHub README

Are you sure? (y/n):
```

---

# Searching Tasks

The search feature allows users to quickly find tasks based on:

* Task name
* Description
* Category

Example:

```text
Enter task to search: Python

Found 2 task(s).
```

---

# Filtering Tasks

Tasks can be filtered according to different conditions.

Example:

```text
1. Pending
2. Completed
3. High Priority
4. Medium Priority
5. Low Priority
6. Category
```

This allows users to focus on specific groups of tasks.

---

# Sorting Tasks

Tasks can be sorted using:

```text
1. Priority
2. Due Date
3. Name
4. Status
```

This provides another way to organize larger task lists.

---

# Saving Tasks

Tasks are automatically saved to:

```text
tasks.json
```

after important changes are made.

This means users do not need to manually save every task.

---

# Loading Tasks

When the Python application starts, previously saved tasks are loaded from:

```text
tasks.json
```

This allows task information to remain available after closing and reopening the program.

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

No external packages are required for the command-line version.

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

## Version 2.5 — Productivity Update

The Python version was further expanded into a more complete productivity application.

### Added

* Productivity Dashboard
* Today's Tasks
* Overdue Tasks
* Upcoming Tasks
* Productivity Score
* Weekly Productivity Report
* Category Summary
* Task Notes
* Focus Task
* Quick Complete for multiple tasks
* Duplicate Tasks
* Completed Task Archiving
* Archived Task Viewer
* Delete All Tasks with confirmation
* Pomodoro Focus Timer
* Productivity Center
* Task Tools menu

The goal of this update was to make the application more useful for everyday task management instead of only functioning as a basic task list.

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
* Modules
* JSON data

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
* Data processing
* Sorting
* Searching
* Filtering

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
* Sorting data
* Tracking task status
* Organizing information
* Archiving information

## File Handling

The Python version demonstrates:

* Creating files
* Reading files
* Writing files
* Saving application data
* Loading saved data
* Working with JSON
* Maintaining separate archive data

## Date and Time

The project also practices Python's date and time functionality for:

* Due dates
* Task creation timestamps
* Today's tasks
* Upcoming tasks
* Overdue task detection
* Weekly reports
* Productivity tracking
* Timer functionality

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

## Productivity Application Design

The newer features introduce concepts used in real productivity applications, including:

* Dashboards
* Progress tracking
* Task prioritization
* Focus management
* Reports
* Task archiving
* Productivity measurements
* Time management

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
17. Build productivity-focused features
18. Work with dates and time
19. Analyze task completion
20. Design features around real-world user needs

---

# Educational Purpose

This project was created primarily for **learning and practice**.

It demonstrates how a beginner programming project can gradually develop into a more complete application.

The project began as a simple Python command-line To-Do List and was later expanded with productivity tools and a web-based application.

The newer Python features demonstrate how basic programming concepts can be combined to create a more practical productivity system.

This progression allows me to practice both **Python programming and frontend web development** while learning how software projects can evolve over time.

As I continue studying Information Technology, more features and improvements may be added.

---

# Future Improvements

Possible future features include:

* [ ] Recurring tasks
* [ ] Advanced task sorting
* [ ] Advanced filtering
* [ ] Task reminders
* [ ] Notification system
* [ ] Calendar integration
* [ ] More detailed productivity analytics
* [ ] Daily productivity reports
* [ ] Monthly productivity reports
* [ ] Custom task statuses
* [ ] Subtasks
* [ ] Task dependencies
* [ ] Multiple focus tasks
* [ ] Custom Pomodoro sessions
* [ ] Break timer
* [ ] SQLite database
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

| Version                    | Status                | Description                                          |
| -------------------------- | --------------------- | ---------------------------------------------------- |
| Python Version             | Completed / Improving | Command-line task management and productivity system |
| Python Productivity Update | Active Development    | Advanced productivity and task-management features   |
| Web Version                | Active Development    | Browser-based task management                        |

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
* Productivity System Design

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

It started as a simple Python command-line To-Do List and has gradually evolved into a project containing both a **Python productivity application and a web application**.

The project reflects my progress as an Information Technology student and my continued learning in **Python, web development, software development, problem solving, productivity application design, and GitHub**.

More features and improvements may be added as I continue learning and developing my programming skills.
