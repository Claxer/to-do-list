# Python & Web To-Do List

A beginner-friendly **To-Do List application available in both Python and Web versions**. The project is designed to help users manage daily tasks, organize priorities, track progress, and improve productivity through a simple and easy-to-use task-management system.

The project originally started as a basic Python command-line application and has gradually been improved with additional task-management and productivity features. A **web version** was later added to provide a more modern, visual, interactive, and student-friendly experience.

The Python version includes features such as **productivity dashboards, today's tasks, overdue tasks, upcoming tasks, task notes, focus tasks, productivity scores, weekly reports, task archiving, multiple-task completion, task progress tracking, time tracking, task tags, deadline reminders, productivity streaks, task restoration, text and CSV exports, a daily task planner, a random pending-task picker, and a Pomodoro focus timer**.

The web version provides a browser-based approach to task management with a modern interface, interactive controls, task organization, and responsive layouts. Both versions are part of the same project but use different technologies and approaches.

This project is part of my learning journey as an **Information Technology student**, where I am practicing programming, web development, problem solving, application design, and GitHub project management.

---

# Features

The project contains two versions:

- **Python Version** — Command-line task management and productivity application.
- **Web Version** — Browser-based task management application with a modern visual interface.

Both versions are designed around the same main purpose: helping users organize and manage their tasks.

---

# Python Version

The Python version is a command-line To-Do List application built using Python's standard library.

It has developed from a simple task list into a more complete **personal productivity system**.

## Task Management

- Add new tasks
- View all tasks
- Mark tasks as completed
- Mark tasks as pending
- Delete individual tasks
- Edit existing tasks
- Duplicate existing tasks
- Clear completed tasks
- Delete all tasks with confirmation
- Track task status
- Track task progress
- Set tasks as In Progress
- Prevent empty tasks from being added
- Generate a suggested daily task plan
- Pick a random pending task to work on next
- Export task information to a CSV file

## Task Organization

Tasks can contain information such as:

- Task name
- Description
- Priority
- Category
- Due date
- Completion status
- Task progress
- Task status
- Creation date
- Completion date
- Notes
- Tags
- Estimated time
- Actual time spent
- Focus status

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

# Task Progress Tracking

The Python version allows users to manually track the progress of individual tasks.

Progress can be set between:

```text
0% - 100%
```

The task status automatically changes depending on its progress.

```text
0%      → Pending
1-99%   → In Progress
100%    → Completed
```

Example:

```text
Task: Finish Python Project
Progress: 75%
Status: In Progress
```

## Progress Viewer

The application can display a visual progress bar for each task.

Example:

```text
1. Finish Python Project

[###############-----] 75%
Status: In Progress
```

---

# Task Status

Tasks can have three main statuses:

```text
Pending
In Progress
Completed
```

Users can manually set a task to **In Progress**, or its status can automatically change when task progress is updated.

---

# Task Tags

Tasks can have multiple tags.

Example:

```text
Tags:
Python, School, Assignment
```

Tags provide additional information about a task and can be used by the task search system.

Examples include:

```text
exam
project
urgent
programming
personal
```

---

# Estimated Task Time

Users can enter an estimated amount of time required to complete a task.

Example:

```text
Estimated Time: 120 minutes
```

This helps users plan their workload.

---

# Time Tracking

The application allows users to record the actual amount of time spent working on a task.

Example:

```text
Estimated Time: 120 minutes
Time Spent: 90 minutes
```

Users can add additional minutes as they continue working.

---

# Productivity Features

The Python version includes additional features designed to help users manage their workload and improve productivity.

## Productivity Dashboard

The **Productivity Dashboard** provides an overview of current tasks.

It displays information such as:

- Total tasks
- Completed tasks
- Pending tasks
- In-progress tasks
- High-priority tasks
- Tasks due today
- Overdue tasks
- Average task progress
- Completion rate
- Visual progress bar

Example:

```text
========== PRODUCTIVITY DASHBOARD ==========

Total Tasks:       15
Completed:         8
Pending:           7
In Progress:       3
High Priority:     3
Due Today:         2
Overdue:           1
Average Progress:  63.5%

Completion Rate: 53.3%

Progress:
[################--------------]
```

## Today's Tasks

Displays pending tasks due on the current date.

## Overdue Tasks

Identifies unfinished tasks whose due dates have passed.

## Upcoming Tasks

Displays pending tasks due within the next seven days.

## Deadline Reminders

Identifies overdue tasks, tasks due today, and tasks approaching their deadlines within the next three days.

## Task Notes

Allows users to attach multiple notes to individual tasks, including instructions, reminders, and project requirements.

## Focus Task

Allows users to choose one task as their main priority, view the current focus task, and remove it when necessary.

## Productivity Score

Calculates a basic productivity score based on the percentage of tasks completed and displays an appropriate progress message.

## Productivity Streak

Tracks consecutive days on which tasks have been completed using task completion timestamps.

## Weekly Productivity Report

Provides a summary of tasks created during the week, completed tasks, and current pending tasks.

## Category Summary

Displays a breakdown of tasks by category, including completed and pending tasks.

## Quick Complete

Allows users to complete multiple tasks by entering several task IDs at once. Completed tasks receive 100% progress and the Completed status.

## Duplicate Tasks

Creates a copy of an existing task. The duplicated task starts as a new pending task with zero progress, zero time spent, and no focus status.

## Task Archiving

Moves completed tasks into `archived_tasks.json` so that previous work can be preserved separately from active tasks.

Users can archive completed tasks, view archived tasks, restore archived tasks, and clear the archive.

## Export Task Report

Generates `task_report.txt`, containing a readable summary of task statistics and individual task details.

## Pomodoro Focus Timer

Provides a basic focus timer with 25-minute, 15-minute, and custom-duration sessions. Users can stop the timer manually with `Ctrl+C`.

---

# Search and Filtering

Users can search for specific tasks using information such as:

- Task name
- Description
- Category
- Tags

Tasks can also be filtered by:

- Completed
- Pending
- High priority
- Medium priority
- Low priority
- Category
- In Progress
- 0% progress
- 50% progress or higher
- Tasks with tags

---

# Sorting

The Python version supports sorting tasks by:

- Priority
- Due date
- Name
- Status
- Progress
- Estimated time

---

# Statistics

The statistics section provides an overview of task progress and workload.

It can display:

- Total tasks
- Completed tasks
- Pending tasks
- In-progress tasks
- High-priority tasks
- Medium-priority tasks
- Low-priority tasks
- Estimated total time
- Total time spent
- Category breakdown

---

# Daily Task Plan

The **Daily Task Plan** suggests an order for completing unfinished tasks. It considers overdue dates, upcoming deadlines, and priority levels.

It displays up to 10 pending tasks with their priorities, due dates, progress, and status.

The plan is a recommendation and does not automatically modify task information.

---

# Random Pending Task Picker

Selects one unfinished task at random to help users decide what to work on next.

Completed tasks are excluded, and a message is displayed if no pending tasks are available.

---

# Export Tasks to CSV

Exports task data to:

```text
tasks_export.csv
```

The export can include task IDs, titles, descriptions, priorities, categories, due dates, statuses, progress, tags, estimated time, time spent, focus status, and creation dates.

The CSV file can be opened using Microsoft Excel or compatible spreadsheet applications.

---

# Persistent Storage

The Python version stores information locally using JSON files.

```text
tasks.json
archived_tasks.json
```

Generated reports and exports use:

```text
task_report.txt
tasks_export.csv
```

The text report and CSV export are generated when their respective options are selected.

---

# Backward Compatibility

The Python version supports older task records by applying default values when newer fields are missing.

Examples of newer fields include:

```text
progress
status
tags
estimated_time
time_spent
focus
```

This helps preserve existing task data as the application evolves.

---

# Input Validation

The application validates common input errors, including:

- Empty task names
- Invalid task numbers
- Invalid menu choices
- Invalid priority selections
- Invalid dates
- Invalid task IDs
- Invalid progress values
- Invalid estimated time
- Invalid time-spent values
- Invalid timer values

Example:

```python
try:
    choice = int(input("Choose an option: "))
except ValueError:
    print("Please enter a valid number.")
```

---

# Error Handling

The application handles common file and input errors, including:

- Missing task files
- Corrupted JSON files
- Invalid dates
- Invalid task IDs
- Invalid numerical input
- Missing archive files
- Corrupted archive files
- Report creation errors
- CSV export errors

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

The web version expands the original command-line To-Do List into a browser-based task-management application.

It was created to provide a more visual and interactive way to organize tasks while allowing me to practice **HTML, CSS, and JavaScript**.

Unlike the Python version, which uses a terminal menu, the web version uses a graphical webpage with interactive controls and organized task information.

The web application is designed to be clean, modern, practical, and student-friendly.

## Web Application Features

The web version focuses on making everyday task management easier through an interactive browser interface.

Its task-management functionality includes:

- Add new tasks
- View existing tasks
- Edit task information
- Mark tasks as completed
- Delete tasks
- Track task status
- Organize tasks by priority
- Use task categories
- Assign due dates
- Search for tasks
- Filter task lists
- Interact with task controls directly on the webpage
- View task information in an organized layout
- Use a responsive interface on supported screen sizes

These features provide the foundation for managing school assignments, personal reminders, programming projects, and everyday responsibilities.

## Modern User Interface

The web version focuses on a more visual experience than the Python command-line application.

The interface is designed around:

- Clean and organized page sections
- Clear task information
- Readable text and spacing
- Consistent colors and styling
- Interactive buttons and controls
- Easy access to task-management actions
- A layout designed for comfortable everyday use

The purpose is to make task management easier to understand without requiring users to navigate a terminal menu.

## Interactive Task Management

Users can interact with tasks directly through the webpage.

Task-management actions are handled through JavaScript, allowing the interface to respond to user interactions without requiring the Python command-line application to run.

This introduces practical concepts such as event handling, functions, application state, and updating webpage elements dynamically.

## Task Organization

The web version uses task information to help users keep their workload organized.

Depending on the fields supported by the current implementation, tasks can be organized using:

- Task title
- Description
- Priority
- Category
- Due date
- Completion status

These fields help users distinguish urgent assignments from less important activities.

## Search and Filtering

The web version provides task discovery tools that help users locate and organize tasks.

Search can be used to find tasks, while filtering helps narrow the displayed task list according to supported task properties.

This is especially useful when the number of tasks increases.

## Responsive Design

The web interface uses CSS to adapt the layout to different screen sizes.

Responsive design helps make the application more comfortable to use on desktop computers, laptops, tablets, and supported mobile browsers.

The actual layout depends on the current CSS implementation and browser capabilities.

## Browser-Based Application

The web version runs in a modern browser and does not require Python to open the webpage.

The main files are:

```text
index.html
style.css
script.js
```

Each file has a separate responsibility:

- `index.html` defines the webpage structure.
- `style.css` controls the visual appearance and responsive layout.
- `script.js` handles task interactions and application logic.

The web version is maintained separately from the Python application, allowing both versions to continue developing without replacing one another.

## Web Technologies

The web version uses:

- **HTML5** — Defines the structure and content of the webpage.
- **CSS3** — Controls styling, spacing, layout, and responsive behavior.
- **JavaScript** — Implements task-management logic and interactive webpage behavior.

No frontend framework is required for the basic web version.

---

# Project Structure

```text
to-do-list/
│
├── python-version/
│   ├── main.py
│   ├── tasks.json
│   ├── archived_tasks.json
│   ├── task_report.txt
│   └── tasks_export.csv
│
├── web-version/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── LICENSE
└── README.md
```

The structure above is an example of how the project can be organized. The actual folders and files should match the current GitHub repository.

## File Description

| File | Description |
|---|---|
| `main.py` | Main Python task-management and productivity application |
| `tasks.json` | Local storage for Python task data |
| `archived_tasks.json` | Storage for archived Python tasks |
| `task_report.txt` | Generated text report |
| `tasks_export.csv` | Generated CSV export |
| `index.html` | Main webpage for the web version |
| `style.css` | Styling and responsive layout for the web version |
| `script.js` | JavaScript functionality for the web version |
| `README.md` | Project documentation |
| `LICENSE` | Project license |

Generated files such as JSON, TXT, and CSV files may appear after using the application.

---

# How the Python Version Works

When the Python application starts, users are presented with a menu containing the available task-management options.

Example:

```text
==================================================
                 TO-DO LIST
==================================================

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
13. Daily Task Plan
14. Pick a Random Pending Task
15. Export Tasks to CSV
16. Exit

Choose an option:
```

The main menu provides access to the original task-management functions and the newer productivity tools.

---

# Productivity Center

The **Productivity Center** groups features focused on planning workloads and improving productivity.

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
9. Deadline Reminders
10. Productivity Streak
11. View Task Progress
12. Export Task Report
13. Back
```

This keeps the main menu organized as more features are added.

---

# Task Tools

The **Task Tools** section contains additional functions for managing individual tasks.

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
11. Update Task Progress
12. Set Task In Progress
13. Add Time Spent
14. Restore Archived Task
15. Clear Archive
16. Back
```

---

# Adding a Task

Users can create a new task by selecting **Add Task**.

The Python application can collect information such as:

- Task name
- Description
- Priority
- Category
- Due date
- Tags
- Estimated time

Example:

```text
Task name: Finish Python assignment
Description: Complete the programming activity
Priority: High
Category: School
Due date: 2026-09-15
Tags: Python, Assignment, School
Estimated time: 120
```

The task is saved to the local JSON file.

---

# Viewing Tasks

The Python application displays tasks and their associated information.

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
Progress: 0%
Estimated Time: 120 minutes
Time Spent: 0 minutes
Tags: Python, Assignment, School
Focus Task: No
Created: 2026-09-13 09:00
```

---

# Completing a Task

When a task is finished, users can mark it as completed.

```text
Enter task ID: 2

Task marked as completed.
```

The task's progress becomes `100%`, and its status becomes `Completed`.

---

# Editing a Task

Users can modify existing task information, including:

- Task name
- Description
- Priority
- Category
- Due date
- Tags
- Estimated time

Users can leave a field blank to keep its existing value, where supported by the Python implementation.

---

# Deleting a Task

Users can remove individual tasks, with confirmation before permanent deletion.

```text
Task: Create GitHub README

Are you sure? (y/n):
```

---

# Searching Tasks

The Python search feature can find tasks based on their names, descriptions, categories, and tags.

Example:

```text
Enter task to search: Python

Found 2 task(s).
```

---

# Filtering Tasks

The Python version supports filtering tasks using:

```text
1. Pending
2. Completed
3. High Priority
4. Medium Priority
5. Low Priority
6. Category
7. In Progress
8. Progress 0%
9. Progress 50% or more
10. Has Tags
```

---

# Sorting Tasks

The Python version supports sorting by:

```text
1. Priority
2. Due Date
3. Name
4. Status
5. Progress
6. Estimated Time
```

---

# Saving Tasks

Python task information is automatically saved to:

```text
tasks.json
```

This allows information to remain available after the program is closed and reopened.

---

# Loading Tasks

When the Python application starts, previously saved tasks are loaded from `tasks.json`.

Archived tasks are stored separately in `archived_tasks.json`.

---

# Web Version Usage

The web version is designed to run directly in a modern browser.

## Option 1 — Open Directly

1. Open the project folder.
2. Navigate to `web-version/`.
3. Open `index.html` in your browser.
4. Use the webpage to manage tasks.

## Option 2 — Use Visual Studio Code

1. Open the project folder in Visual Studio Code.
2. Navigate to `web-version/index.html`.
3. Open the HTML file in a browser.
4. Alternatively, use an extension such as Live Server to launch a local development server.

No Python installation is required to open the basic web interface.

**Storage note:** Browser-based task persistence depends on how the current JavaScript implementation saves data. If it uses `localStorage`, task data is stored in that browser on that device and is not automatically synchronized with the Python JSON files.

---

# Requirements

## Python Version

- Python 3.x
- Git (optional)

The Python version uses the standard library for its core functionality and does not require external packages for the command-line application.

## Web Version

- A modern web browser
- HTML5 support
- CSS3 support
- JavaScript support
- Visual Studio Code (optional)
- Live Server extension (optional)

---

# Development History

This project was developed progressively as a learning project.

## Version 1.0 — Basic Python To-Do List

### Included

- Add tasks
- View tasks
- Complete tasks
- Delete tasks
- Clear tasks
- Basic menu system

## Version 2.0 — Improved Python To-Do List

### Added

- Task priorities
- Task categories
- Task descriptions
- Due dates
- Edit tasks
- Search tasks
- Filter tasks
- Persistent storage
- Input validation
- Error handling
- Improved task organization

## Version 2.5 — Productivity Update

### Added

- Productivity Dashboard
- Today's Tasks
- Overdue Tasks
- Upcoming Tasks
- Productivity Score
- Weekly Productivity Report
- Category Summary
- Task Notes
- Focus Task
- Quick Complete for multiple tasks
- Duplicate Tasks
- Completed Task Archiving
- Archived Task Viewer
- Delete All Tasks with confirmation
- Pomodoro Focus Timer
- Productivity Center
- Task Tools menu

## Version 3.0 — Advanced Productivity Update

### Added

- Task progress tracking
- Automatic Pending / In Progress / Completed statuses
- Progress percentage
- Visual task progress bars
- Task tags
- Tag-based searching
- Estimated task time
- Actual time tracking
- Time-spent statistics
- Deadline reminders
- Productivity streak tracking
- Restore archived tasks
- Clear archived tasks
- Task report exporting
- Expanded task filtering
- Expanded task sorting
- Improved productivity dashboard
- Improved task statistics
- Backward-compatible task data handling

## Version 3.1 — Task Planning and Export Update

### Added

- Daily Task Plan ordered by overdue status, due date, and priority
- Random Pending Task Picker
- CSV export to `tasks_export.csv`
- Main-menu options for accessing the new tools
- Handling for empty task lists and CSV file-writing errors

## Version 4.0 — Web Version

The project was expanded from a command-line application into a browser-based application.

### Added

- HTML interface
- CSS styling
- JavaScript functionality
- Modern visual interface
- Student-friendly design
- Interactive task management
- Browser-based task organization
- Responsive layout
- Improved user experience
- Separate frontend project files
- Browser-based access to task-management controls

The web version provides a new way to interact with the project while preserving the Python application's original functionality.

---

# Learning Objectives

This project helps develop practical programming and web-development skills.

## Python Fundamentals

- Variables
- Strings
- Integers
- Booleans
- Lists
- Dictionaries
- Functions
- Loops
- Conditional statements
- Modules
- JSON data

## Programming Logic

- `if`, `elif`, and `else`
- `for` loops
- `while` loops
- Functions
- Menu-based program logic
- Data processing
- Random selection
- Sorting
- Searching
- Filtering
- Progress calculations
- Date calculations
- Time calculations

## User Input

- Receiving user input
- Validating input
- Converting input types
- Handling invalid input
- Creating interactive command-line programs

## Data Management

- Adding data
- Updating data
- Removing data
- Searching data
- Filtering data
- Sorting data
- Tracking task status
- Tracking progress
- Tracking time
- Organizing information
- Archiving information
- Restoring archived information

## File Handling

- Creating files
- Reading files
- Writing files
- Saving application data
- Loading saved data
- Working with JSON
- Maintaining separate archive data
- Generating text reports
- Exporting structured task data to CSV

## Date and Time

- Due dates
- Task creation timestamps
- Task completion timestamps
- Today's tasks
- Upcoming tasks
- Overdue task detection
- Weekly reports
- Productivity streaks
- Timer functionality

## Web Development

- HTML structure
- CSS styling
- JavaScript programming
- DOM manipulation
- Event handling
- Interactive webpage elements
- Responsive design
- Frontend application development
- User interface design

## Productivity Application Design

- Dashboards
- Progress tracking
- Task prioritization
- Focus management
- Reports
- Task archiving
- Productivity measurements
- Time management
- Deadline management
- Task categorization
- Task tagging
- Workload tracking

---

# GitHub Learning

This project is also part of my learning journey with **Git and GitHub**.

Skills practiced include:

- Creating repositories
- Creating README files
- Organizing project files
- Creating project folders
- Committing changes
- Writing commit messages
- Pushing code to GitHub
- Updating existing projects
- Versioning projects
- Documenting software projects

---

# Project Goals

The main goal of this project is to continuously improve my programming and application-development skills.

Through this project, I am practicing how to:

1. Build an application from scratch.
2. Plan application functionality.
3. Organize project files.
4. Write Python code.
5. Write HTML and CSS.
6. Use JavaScript.
7. Create reusable functions.
8. Work with data.
9. Handle user input.
10. Validate information.
11. Implement application logic.
12. Create interactive web applications.
13. Debug applications.
14. Use Git and GitHub.
15. Document software projects.
16. Improve an application through multiple versions.
17. Build productivity-focused features.
18. Work with dates and time.
19. Analyze task completion.
20. Design features around real-world user needs.
21. Track task progress.
22. Track estimated and actual work time.
23. Build simple productivity analytics.
24. Work with archived application data.
25. Generate application reports.
26. Practice frontend development.
27. Improve user interface design.
28. Build and maintain separate Python and web versions of the same project.

---

# Educational Purpose

This project was created primarily for **learning and practice**.

It demonstrates how a beginner programming project can gradually develop into a more complete application.

The project began as a simple Python command-line To-Do List and was later expanded with productivity tools and a web-based application.

The Python version demonstrates how fundamental programming concepts can be combined to build a more complete productivity system, while the web version provides practical experience with frontend development and interactive interfaces.

This progression allows me to practice both **Python programming and frontend web development** while learning how software projects can evolve over time.

As I continue studying Information Technology, more features and improvements may be added.

---

# Future Improvements

Possible future features include:

- [ ] Recurring tasks
- [ ] Advanced task sorting
- [ ] Advanced filtering
- [ ] Task reminders
- [ ] Notification system
- [ ] Calendar integration
- [ ] More detailed productivity analytics
- [ ] Daily productivity reports
- [ ] Monthly productivity reports
- [ ] Custom task statuses
- [ ] Subtasks
- [ ] Task dependencies
- [ ] Multiple focus tasks
- [ ] Custom Pomodoro sessions
- [ ] Break timer
- [ ] SQLite database
- [ ] User accounts
- [ ] Login system
- [ ] Desktop application
- [ ] Mobile version
- [ ] Cloud synchronization
- [ ] Backend integration
- [ ] Online database
- [ ] User authentication
- [ ] Cross-device synchronization

---

# Project Status

**Current Status: Active Development**

The project is continuously being improved as I learn new programming and web-development concepts.

| Version | Status | Description |
|---|---|---|
| Python Version | Completed / Improving | Command-line task management and productivity system |
| Python Productivity Update | Active Development | Advanced productivity and task-management features |
| Web Version | Active Development | Browser-based task management and frontend development |

---

# Author

**Jose Navoa**

Student Developer

This project is part of my learning journey in:

- Information Technology
- Python Programming
- Web Development
- HTML
- CSS
- JavaScript
- Software Development
- Problem Solving
- Git and GitHub
- Application Development
- Productivity System Design

---

# License

This project is intended for **educational and personal use**.

You are welcome to:

- Study the code
- Modify the code
- Experiment with new features
- Use the project as a learning reference
- Improve the application

Please refer to the repository's `LICENSE` file for the applicable license terms.

---

# Acknowledgments

This project was created as a beginner-to-intermediate programming project.

It started as a simple Python command-line To-Do List and has gradually evolved into a project containing both a **Python productivity application and a web application**.

The project reflects my progress as an Information Technology student and my continued learning in **Python, web development, software development, problem solving, productivity application design, and GitHub**.

More features and improvements may be added as I continue learning and developing my programming skills.
