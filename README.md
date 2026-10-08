# Python & Web To-Do List

A beginner-friendly **To-Do List application available in both Python and Web versions**. The project is designed to help users manage daily tasks, organize priorities, track progress, and improve productivity through a simple and easy-to-use task-management system.

The project originally started as a basic Python command-line application and has gradually been improved with additional task-management and productivity features. A **web version** was later added to provide a more modern, visual, and student-friendly experience.

The Python version now includes features such as **productivity dashboards, today's tasks, overdue tasks, upcoming tasks, task notes, focus tasks, productivity scores, weekly reports, task archiving, multiple-task completion, task progress tracking, time tracking, task tags, deadline reminders, productivity streaks, task restoration, text and CSV exports, a daily task planner, a random pending-task picker, and a Pomodoro focus timer**.

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
* Track task progress
* Set tasks as In Progress
* Prevent empty tasks from being added
* Generate a suggested daily task plan
* Pick a random pending task to work on next
* Export task information to a CSV file

## Task Organization

Tasks can contain information such as:

* Task name
* Description
* Priority
* Category
* Due date
* Completion status
* Task progress
* Task status
* Creation date
* Completion date
* Notes
* Tags
* Estimated time
* Actual time spent
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

# Task Progress Tracking

The Python version now allows users to manually track the progress of individual tasks.

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

This provides more information than simply using completed or pending.

## Progress Viewer

The application can display a visual progress bar for each task.

Example:

```text
1. Finish Python Project

[###############-----] 75%
Status: In Progress
```

This makes it easier to see how much work has been completed.

---

# Task Status

Tasks can now have different statuses.

Current statuses include:

```text
Pending
In Progress
Completed
```

Users can manually set a task to **In Progress**, or the status can automatically change when task progress is updated.

This gives users a better understanding of which tasks have been started and which ones have not.

---

# Task Tags

Tasks can now have multiple tags.

Example:

```text
Tags:
Python, School, Assignment
```

Tags can be used to provide additional information about a task.

For example:

```text
exam
project
urgent
programming
personal
```

Tags are also included in the task search system, making it easier to find tasks based on specific labels.

---

# Estimated Task Time

Users can now enter an estimated amount of time required to complete a task.

Example:

```text
Estimated Time: 120 minutes
```

This can help users plan their workload and understand how much time their tasks may require.

---

# Time Tracking

The application now allows users to record the actual amount of time spent working on a task.

Example:

```text
Estimated Time: 120 minutes
Time Spent: 90 minutes
```

Users can add additional minutes as they continue working on a task.

This provides a basic way to compare estimated work time with actual work time.

---

# Productivity Features

The Python version now includes additional features designed to help users manage their workload and become more productive.

## Productivity Dashboard

The **Productivity Dashboard** provides a quick overview of the user's current tasks.

It displays information such as:

* Total tasks
* Completed tasks
* Pending tasks
* In-progress tasks
* High-priority tasks
* Tasks due today
* Overdue tasks
* Average task progress
* Completion rate
* Visual progress bar

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

# Deadline Reminders

The new **Deadline Reminders** feature checks tasks that are overdue or approaching their due dates.

The application identifies:

* Overdue tasks
* Tasks due today
* Tasks due within the next three days

Example:

```text
========== DEADLINE REMINDERS ==========

OVERDUE: Finish Database Activity
Due: 2026-09-12

DUE TODAY: Submit Assignment

DUE SOON: Prepare Presentation
Due in 2 day(s)
```

This gives users a quick reminder of deadlines that require attention.

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

# Productivity Streak

The new **Productivity Streak** feature tracks consecutive days on which tasks have been completed.

Example:

```text
========== PRODUCTIVITY STREAK ==========

Current Productivity Streak: 5 day(s)

Great consistency!
```

The feature encourages users to maintain consistent productivity habits.

Task completion timestamps are used to determine completion dates.

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

When tasks are completed using this feature, their progress is also updated to **100%** and their status becomes **Completed**.

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

The duplicated task starts as a new pending task with:

```text
Progress: 0%
Status: Pending
Time Spent: 0 minutes
Focus: No
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
* Restore archived tasks
* Keep completed work separate from current tasks
* Clear the archive when needed

This helps keep the main task list clean while preserving previous tasks.

---

# Restore Archived Tasks

The new **Restore Archived Task** feature allows users to bring a task back from the archive.

Example:

```text
========== RESTORE ARCHIVED TASK ==========

1. Finish Python Assignment
2. Submit Database Project

Enter archived task ID to restore:
```

When restored, the task becomes a new active task with:

```text
Status: Pending
Progress: 0%
Focus: No
```

This allows previously archived work to be reused when necessary.

---

# Clear Archive

Users can permanently remove all archived tasks.

The application requires the user to type:

```text
CLEAR
```

before the archive is permanently cleared.

This confirmation helps prevent accidental deletion.

---

# Export Task Report

The application now allows users to export their current tasks into a text report.

The report is saved as:

```text
task_report.txt
```

The exported text report contains information such as:

* Total tasks
* Completed tasks
* Pending tasks
* Task names
* Descriptions
* Priorities
* Categories
* Due dates
* Status
* Progress
* Estimated time
* Actual time spent
* Tags

Example:

```text
TO-DO LIST PRODUCTIVITY REPORT
==================================================

Generated: 2026-09-14 18:00

Total Tasks: 15
Completed: 8
Pending: 7

TASK DETAILS
==================================================
```

This provides a simple way to create a readable backup or summary of the current task list.

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
* In Progress
* 0% progress
* 50% progress or higher
* Tasks with tags

Search can also find tasks using their tags.

For example, searching for:

```text
Python
```

can find a task where `Python` is included in its title, description, category, or tags.

This makes the search system more useful as the task list becomes larger.

---

# Sorting

The Python version can organize tasks using different sorting methods.

Available sorting options include:

* Priority
* Due date
* Name
* Status
* Progress
* Estimated time

This allows users to organize their task list based on what they need to focus on.

For example, users can sort by progress to see which tasks are closest to completion.

---

# Statistics

The application includes a statistics section that provides an overview of the user's tasks.

It can display:

* Total tasks
* Completed tasks
* Pending tasks
* In-progress tasks
* High-priority tasks
* Medium-priority tasks
* Low-priority tasks
* Estimated total time
* Total time spent
* Category breakdown

Example:

```text
========== TASK STATISTICS ==========

Total Tasks: 15
Completed: 8
Pending: 7
In Progress: 3

Priority Breakdown:
High: 4
Medium: 6
Low: 5

Time Tracking:
Estimated Time: 900 minutes
Time Spent: 620 minutes
```

This provides a more detailed overview of how tasks and time are being managed.

---

# Daily Task Plan

The **Daily Task Plan** creates a suggested order for working through unfinished tasks. It considers overdue tasks first, then due dates, and then priority levels (**High**, **Medium**, and **Low**). It displays up to 10 pending tasks, including each task's priority, due date, progress, and status.

Example:

```text
========== DAILY TASK PLAN ==========
Suggested order based on overdue dates, deadlines, and priority:

1. Finish Database Activity
   Priority: High | Due: 2026-10-08
   Progress: 25% | Status: In Progress
```

Choose **Daily Task Plan** from the main menu to view the suggested order. The plan is a recommendation; it does not change task details or automatically mark tasks as complete.

---

# Random Pending Task Picker

The **Pick a Random Pending Task** feature chooses one unfinished task at random. It can be useful when users are unsure which pending task to work on next. The selected task is displayed using the application's existing task display format. Completed tasks are not included in the selection.

If there are no pending tasks, the application displays a message instead of selecting a task.

---

# Export Tasks to CSV

The Python version can export task data to a comma-separated values (**CSV**) file named:

```text
tasks_export.csv
```

The export includes fields such as task ID, title, description, priority, category, due date, completion status, progress, tags, estimated time, time spent, focus status, and creation date. The CSV file can be opened in spreadsheet applications such as Microsoft Excel or compatible programs.

To create the file, choose **Export Tasks to CSV** from the main menu. If there are no tasks to export, the application informs the user. The export also handles file-writing errors by displaying an error message.

This is separate from `task_report.txt`: the text report provides a readable summary, while the CSV export organizes individual task fields into columns.

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

Generated reports can be saved using:

```text
task_report.txt
```

Task data can also be exported for spreadsheet use to:

```text
tasks_export.csv
```

The CSV file is generated when the user selects the export option. This provides persistent local storage and export options without requiring a database.

---

# Backward Compatibility

The newer features were designed to work with the original task structure.

Existing tasks that were created before the newer features were added can still be loaded.

For example, if an older task does not contain:

```text
progress
status
tags
estimated_time
time_spent
focus
```

the application uses default values when necessary.

This allows the project to continue developing without requiring the original task data to be completely recreated.

---

# Input Validation

The application includes validation for common input errors, including:

* Empty task names
* Invalid task numbers
* Invalid menu choices
* Invalid priority selections
* Invalid date input
* Invalid task IDs
* Invalid progress values
* Invalid estimated time
* Invalid time spent values
* Invalid timer values

Example:

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
* Missing archive files
* Corrupted archive files
* Report creation errors

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
│   ├── archived_tasks.json
│   └── task_report.txt
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
| `task_report.txt`     | Generated text report of current tasks              |
| `tasks_export.csv`    | Generated CSV export of task details                |
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

The main menu keeps the original task-management functions while grouping productivity tools in dedicated sections. The three additional options provide a daily task plan, a random task suggestion, and a CSV export.

---

# Productivity Center

The **Productivity Center** contains features focused on helping users plan their workload and improve productivity.

The updated Productivity Center includes:

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

This keeps the main menu organized even as more features are added.

---

# Task Tools

The **Task Tools** section contains additional tools for managing individual tasks.

The updated Task Tools menu includes:

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
* Tags
* Estimated time

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

The task is then saved to the local JSON file.

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

The task remains in the list while its completion status changes.

When completed, the task's progress is automatically set to:

```text
100%
```

and its status becomes:

```text
Completed
```

---

# Editing a Task

Users can modify an existing task.

Possible information to change includes:

* Task name
* Description
* Priority
* Category
* Due date
* Tags
* Estimated time

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
* Tags

Example:

```text
Enter task to search: Python

Found 2 task(s).
```

---

# Filtering Tasks

Tasks can be filtered according to different conditions.

The updated filtering system includes:

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

This allows users to focus on specific groups of tasks.

---

# Sorting Tasks

Tasks can be sorted using:

```text
1. Priority
2. Due Date
3. Name
4. Status
5. Progress
6. Estimated Time
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

## Version 3.0 — Advanced Productivity Update

The Python application was further improved with more detailed task tracking and productivity tools.

### Added

* Task progress tracking
* Automatic Pending / In Progress / Completed statuses
* Progress percentage
* Visual task progress bars
* Task tags
* Tag-based searching
* Estimated task time
* Actual time tracking
* Time-spent statistics
* Deadline reminders
* Productivity streak tracking
* Restore archived tasks
* Clear archived tasks
* Task report exporting
* Expanded task filtering
* Expanded task sorting
* Improved productivity dashboard
* Improved task statistics
* Backward-compatible task data handling

These features transformed the Python version from a traditional To-Do List into a more complete **personal productivity and task-management system**.

---

## Version 3.1 — Task Planning and Export Update

The Python version received three additional tools to make daily task management more convenient.

### Added

* Daily Task Plan ordered by overdue status, due date, and priority
* Random Pending Task Picker
* CSV export of task information to `tasks_export.csv`
* Main-menu options for accessing the new tools
* Basic handling for empty task lists and CSV file-writing errors

The update adds ways to decide what to work on next and to use task data outside the application.

---

## Version 4.0 — Web Version

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
* Random selection from a filtered task list
* Ordering tasks using multiple conditions
* Sorting
* Searching
* Filtering
* Progress calculations
* Date calculations
* Time calculations

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
* Tracking progress
* Tracking time
* Organizing information
* Archiving information
* Restoring archived information

## File Handling

The Python version demonstrates:

* Creating files
* Reading files
* Writing files
* Saving application data
* Loading saved data
* Working with JSON
* Maintaining separate archive data
* Generating text reports
* Exporting structured task data to CSV

## Date and Time

The project also practices Python's date and time functionality for:

* Due dates
* Task creation timestamps
* Task completion timestamps
* Today's tasks
* Upcoming tasks
* Overdue task detection
* Weekly reports
* Productivity streaks
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
* Deadline management
* Task categorization
* Task tagging
* Workload tracking

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
21. Track task progress
22. Track estimated and actual work time
23. Build simple productivity analytics
24. Work with archived application data
25. Generate application reports

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
