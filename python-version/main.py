import json
import time
from datetime import datetime, date, timedelta

FILE_NAME = "tasks.json"
ARCHIVE_FILE = "archived_tasks.json"


# ==========================================
# LOAD TASKS
# ==========================================

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Warning: Task file is corrupted.")
        return []


# ==========================================
# SAVE TASKS
# ==========================================

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# ==========================================
# GENERATE TASK ID
# ==========================================

def generate_task_id(tasks):

    if not tasks:
        return 1

    return max(task["id"] for task in tasks) + 1


# ==========================================
# ADD TASK
# ==========================================

def add_task(tasks):

    print("\n========== ADD TASK ==========")

    title = input("Task name: ").strip()

    if not title:
        print("Task name cannot be empty.")
        return

    description = input("Description: ").strip()

    # Priority
    while True:

        priority = input(
            "Priority (Low / Medium / High): "
        ).strip().capitalize()

        if priority in ["Low", "Medium", "High"]:
            break

        print("Please choose Low, Medium, or High.")

    # Category
    category = input(
        "Category (School / Work / Personal / Other): "
    ).strip().capitalize()

    if not category:
        category = "Other"

    # Due date
    while True:

        due_date = input(
            "Due date (YYYY-MM-DD) or leave blank: "
        ).strip()

        if due_date == "":
            break

        try:
            datetime.strptime(due_date, "%Y-%m-%d")
            break

        except ValueError:
            print("Invalid date format.")

    task = {
        "id": generate_task_id(tasks),
        "title": title,
        "description": description,
        "priority": priority,
        "category": category,
        "due_date": due_date,
        "completed": False,
        "created_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M"
        )
    }

    tasks.append(task)

    save_tasks(tasks)

    print("\nTask added successfully.")


# ==========================================
# DISPLAY TASK
# ==========================================

def display_task(task):

    status = "Completed" if task["completed"] else "Pending"

    print(
        f"\nID: {task['id']}"
        f"\nTask: {task['title']}"
        f"\nDescription: {task['description']}"
        f"\nPriority: {task['priority']}"
        f"\nCategory: {task['category']}"
        f"\nDue Date: {task['due_date'] or 'None'}"
        f"\nStatus: {status}"
        f"\nCreated: {task['created_at']}"
    )


# ==========================================
# VIEW ALL TASKS
# ==========================================

def view_tasks(tasks):

    print("\n========== ALL TASKS ==========")

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        display_task(task)
        print("-" * 35)


# ==========================================
# FIND TASK
# ==========================================

def find_task(tasks, task_id):

    for task in tasks:

        if task["id"] == task_id:
            return task

    return None


# ==========================================
# COMPLETE / UNCOMPLETE TASK
# ==========================================

def toggle_task(tasks):

    print("\n========== CHANGE TASK STATUS ==========")

    if not tasks:
        print("No tasks available.")
        return

    try:
        task_id = int(
            input("Enter task ID: ")
        )

    except ValueError:
        print("Please enter a valid number.")
        return

    task = find_task(tasks, task_id)

    if task is None:
        print("Task not found.")
        return

    task["completed"] = not task["completed"]

    save_tasks(tasks)

    if task["completed"]:
        print("Task marked as completed.")

    else:
        print("Task marked as pending.")


# ==========================================
# EDIT TASK
# ==========================================

def edit_task(tasks):

    print("\n========== EDIT TASK ==========")

    if not tasks:
        print("No tasks available.")
        return

    try:
        task_id = int(
            input("Enter task ID: ")
        )

    except ValueError:
        print("Invalid task ID.")
        return

    task = find_task(tasks, task_id)

    if task is None:
        print("Task not found.")
        return

    print("\nLeave a field blank to keep its current value.")

    new_title = input(
        f"Task name [{task['title']}]: "
    ).strip()

    if new_title:
        task["title"] = new_title

    new_description = input(
        f"Description [{task['description']}]: "
    ).strip()

    if new_description:
        task["description"] = new_description

    # Priority
    while True:

        new_priority = input(
            f"Priority [{task['priority']}] "
            "(Low / Medium / High): "
        ).strip().capitalize()

        if new_priority == "":
            break

        if new_priority in ["Low", "Medium", "High"]:
            task["priority"] = new_priority
            break

        print("Invalid priority.")

    new_category = input(
        f"Category [{task['category']}]: "
    ).strip().capitalize()

    if new_category:
        task["category"] = new_category

    # Due date
    while True:

        new_due_date = input(
            f"Due date [{task['due_date'] or 'None'}]: "
        ).strip()

        if new_due_date == "":
            break

        try:
            datetime.strptime(
                new_due_date,
                "%Y-%m-%d"
            )

            task["due_date"] = new_due_date
            break

        except ValueError:
            print("Invalid date.")

    save_tasks(tasks)

    print("Task updated successfully.")


# ==========================================
# DELETE TASK
# ==========================================

def delete_task(tasks):

    print("\n========== DELETE TASK ==========")

    if not tasks:
        print("No tasks available.")
        return

    try:
        task_id = int(
            input("Enter task ID: ")
        )

    except ValueError:
        print("Invalid task ID.")
        return

    task = find_task(tasks, task_id)

    if task is None:
        print("Task not found.")
        return

    print(f"\nTask: {task['title']}")

    confirmation = input(
        "Are you sure? (y/n): "
    ).lower()

    if confirmation == "y":

        tasks.remove(task)

        save_tasks(tasks)

        print("Task deleted successfully.")

    else:
        print("Delete cancelled.")


# ==========================================
# SEARCH TASKS
# ==========================================

def search_tasks(tasks):

    print("\n========== SEARCH TASKS ==========")

    search = input(
        "Search: "
    ).strip().lower()

    results = []

    for task in tasks:

        if (
            search in task["title"].lower()
            or search in task["description"].lower()
            or search in task["category"].lower()
        ):
            results.append(task)

    if not results:

        print("No matching tasks found.")
        return

    print(
        f"\nFound {len(results)} task(s)."
    )

    for task in results:

        display_task(task)

        print("-" * 35)


# ==========================================
# FILTER TASKS
# ==========================================

def filter_tasks(tasks):

    print("\n========== FILTER TASKS ==========")

    print("1. Pending")
    print("2. Completed")
    print("3. High Priority")
    print("4. Medium Priority")
    print("5. Low Priority")
    print("6. Category")

    choice = input(
        "\nChoose filter: "
    )

    results = []

    if choice == "1":

        results = [
            task for task in tasks
            if not task["completed"]
        ]

    elif choice == "2":

        results = [
            task for task in tasks
            if task["completed"]
        ]

    elif choice == "3":

        results = [
            task for task in tasks
            if task["priority"] == "High"
        ]

    elif choice == "4":

        results = [
            task for task in tasks
            if task["priority"] == "Medium"
        ]

    elif choice == "5":

        results = [
            task for task in tasks
            if task["priority"] == "Low"
        ]

    elif choice == "6":

        category = input(
            "Enter category: "
        ).strip().lower()

        results = [
            task for task in tasks
            if task["category"].lower() == category
        ]

    else:

        print("Invalid option.")
        return

    if not results:

        print("No tasks found.")
        return

    for task in results:

        display_task(task)

        print("-" * 35)


# ==========================================
# SORT TASKS
# ==========================================

def sort_tasks(tasks):

    print("\n========== SORT TASKS ==========")

    print("1. Priority")
    print("2. Due Date")
    print("3. Name")
    print("4. Status")

    choice = input(
        "Choose sorting method: "
    )

    if choice == "1":

        priority_order = {
            "High": 1,
            "Medium": 2,
            "Low": 3
        }

        sorted_tasks = sorted(
            tasks,
            key=lambda task:
            priority_order[task["priority"]]
        )

    elif choice == "2":

        sorted_tasks = sorted(
            tasks,
            key=lambda task:
            task["due_date"] or "9999-12-31"
        )

    elif choice == "3":

        sorted_tasks = sorted(
            tasks,
            key=lambda task:
            task["title"].lower()
        )

    elif choice == "4":

        sorted_tasks = sorted(
            tasks,
            key=lambda task:
            task["completed"]
        )

    else:

        print("Invalid option.")
        return

    for task in sorted_tasks:

        display_task(task)

        print("-" * 35)


# ==========================================
# STATISTICS
# ==========================================

def show_statistics(tasks):

    print("\n========== TASK STATISTICS ==========")

    total = len(tasks)

    completed = sum(
        1 for task in tasks
        if task["completed"]
    )

    pending = total - completed

    high = sum(
        1 for task in tasks
        if task["priority"] == "High"
    )

    medium = sum(
        1 for task in tasks
        if task["priority"] == "Medium"
    )

    low = sum(
        1 for task in tasks
        if task["priority"] == "Low"
    )

    categories = {}

    for task in tasks:

        category = task["category"]

        categories[category] = (
            categories.get(category, 0) + 1
        )

    print(f"Total Tasks: {total}")
    print(f"Completed: {completed}")
    print(f"Pending: {pending}")

    print("\nPriority Breakdown:")
    print(f"High: {high}")
    print(f"Medium: {medium}")
    print(f"Low: {low}")

    print("\nCategories:")

    if categories:

        for category, amount in categories.items():

            print(
                f"{category}: {amount}"
            )

    else:

        print("No categories yet.")


# ==========================================
# CLEAR COMPLETED TASKS
# ==========================================

def clear_completed(tasks):

    print("\n========== CLEAR COMPLETED ==========")

    completed_tasks = [
        task for task in tasks
        if task["completed"]
    ]

    if not completed_tasks:

        print("There are no completed tasks.")
        return

    print(
        f"There are {len(completed_tasks)} "
        "completed task(s)."
    )

    confirmation = input(
        "Delete all completed tasks? (y/n): "
    ).lower()

    if confirmation == "y":

        tasks[:] = [
            task for task in tasks
            if not task["completed"]
        ]

        save_tasks(tasks)

        print("Completed tasks deleted.")

    else:

        print("Operation cancelled.")


# ==========================================
# NEW FEATURE: DASHBOARD
# ==========================================

def productivity_dashboard(tasks):

    print("\n========== PRODUCTIVITY DASHBOARD ==========")

    total = len(tasks)

    completed = sum(
        1 for task in tasks
        if task["completed"]
    )

    pending = sum(
        1 for task in tasks
        if not task["completed"]
    )

    high_priority = sum(
        1 for task in tasks
        if task["priority"] == "High"
        and not task["completed"]
    )

    today = date.today().strftime("%Y-%m-%d")

    due_today = sum(
        1 for task in tasks
        if task["due_date"] == today
        and not task["completed"]
    )

    overdue = 0

    for task in tasks:

        if task["completed"]:
            continue

        if task["due_date"]:

            try:

                due = datetime.strptime(
                    task["due_date"],
                    "%Y-%m-%d"
                ).date()

                if due < date.today():
                    overdue += 1

            except ValueError:
                pass

    if total > 0:
        completion_rate = (
            completed / total
        ) * 100
    else:
        completion_rate = 0

    print(f"\nTotal Tasks:       {total}")
    print(f"Completed:         {completed}")
    print(f"Pending:           {pending}")
    print(f"High Priority:     {high_priority}")
    print(f"Due Today:         {due_today}")
    print(f"Overdue:           {overdue}")

    print(
        f"\nCompletion Rate: {completion_rate:.1f}%"
    )

    print("\nProgress:")

    bar_size = 30

    filled = int(
        completion_rate / 100 * bar_size
    )

    bar = "#" * filled + "-" * (
        bar_size - filled
    )

    print(f"[{bar}]")

    print("=" * 50)


# ==========================================
# NEW FEATURE: TODAY'S TASKS
# ==========================================

def todays_tasks(tasks):

    print("\n========== TODAY'S TASKS ==========")

    today = date.today().strftime("%Y-%m-%d")

    results = [
        task for task in tasks
        if task["due_date"] == today
        and not task["completed"]
    ]

    if not results:

        print("No pending tasks are due today.")
        return

    print(
        f"\nYou have {len(results)} task(s) "
        "due today."
    )

    for task in results:

        display_task(task)

        print("-" * 35)


# ==========================================
# NEW FEATURE: OVERDUE TASKS
# ==========================================

def overdue_tasks(tasks):

    print("\n========== OVERDUE TASKS ==========")

    results = []

    today = date.today()

    for task in tasks:

        if task["completed"]:
            continue

        if not task["due_date"]:
            continue

        try:

            due = datetime.strptime(
                task["due_date"],
                "%Y-%m-%d"
            ).date()

            if due < today:
                results.append(task)

        except ValueError:
            pass

    if not results:

        print("You have no overdue tasks.")
        return

    print(
        f"\nYou have {len(results)} overdue task(s)."
    )

    for task in results:

        display_task(task)

        print("-" * 35)


# ==========================================
# NEW FEATURE: UPCOMING TASKS
# ==========================================

def upcoming_tasks(tasks):

    print("\n========== UPCOMING TASKS ==========")

    today = date.today()
    next_week = today + timedelta(days=7)

    results = []

    for task in tasks:

        if task["completed"]:
            continue

        if not task["due_date"]:
            continue

        try:

            due = datetime.strptime(
                task["due_date"],
                "%Y-%m-%d"
            ).date()

            if today <= due <= next_week:
                results.append(task)

        except ValueError:
            pass

    if not results:

        print("No tasks due within the next 7 days.")
        return

    results.sort(
        key=lambda task: task["due_date"]
    )

    for task in results:

        display_task(task)

        print("-" * 35)


# ==========================================
# NEW FEATURE: ADD TASK NOTES
# ==========================================

def add_task_note(tasks):

    print("\n========== ADD TASK NOTE ==========")

    try:

        task_id = int(
            input("Enter task ID: ")
        )

    except ValueError:

        print("Invalid task ID.")
        return

    task = find_task(tasks, task_id)

    if task is None:

        print("Task not found.")
        return

    note = input(
        "Enter note: "
    ).strip()

    if not note:

        print("Note cannot be empty.")
        return

    if "notes" not in task:

        task["notes"] = []

    task["notes"].append({
        "text": note,
        "created_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M"
        )
    })

    save_tasks(tasks)

    print("Note added successfully.")


# ==========================================
# NEW FEATURE: VIEW TASK NOTES
# ==========================================

def view_task_notes(tasks):

    print("\n========== TASK NOTES ==========")

    try:

        task_id = int(
            input("Enter task ID: ")
        )

    except ValueError:

        print("Invalid task ID.")
        return

    task = find_task(tasks, task_id)

    if task is None:

        print("Task not found.")
        return

    notes = task.get("notes", [])

    if not notes:

        print("This task has no notes.")
        return

    print(f"\nTask: {task['title']}")

    for number, note in enumerate(notes, 1):

        print(
            f"\n{number}. {note['text']}"
        )

        print(
            f"   Added: {note['created_at']}"
        )


# ==========================================
# NEW FEATURE: DUPLICATE TASK
# ==========================================

def duplicate_task(tasks):

    print("\n========== DUPLICATE TASK ==========")

    try:

        task_id = int(
            input("Enter task ID: ")
        )

    except ValueError:

        print("Invalid task ID.")
        return

    task = find_task(tasks, task_id)

    if task is None:

        print("Task not found.")
        return

    new_task = task.copy()

    new_task["id"] = generate_task_id(tasks)

    new_task["title"] = (
        task["title"] + " (Copy)"
    )

    new_task["completed"] = False

    new_task["created_at"] = (
        datetime.now().strftime(
            "%Y-%m-%d %H:%M"
        )
    )

    tasks.append(new_task)

    save_tasks(tasks)

    print("Task duplicated successfully.")


# ==========================================
# NEW FEATURE: COMPLETE MULTIPLE TASKS
# ==========================================

def quick_complete(tasks):

    print("\n========== QUICK COMPLETE ==========")

    if not tasks:

        print("No tasks available.")
        return

    print(
        "Enter task IDs separated by commas."
    )

    print(
        "Example: 1, 3, 5"
    )

    user_input = input(
        "Task IDs: "
    )

    ids = user_input.split(",")

    completed_count = 0

    for item in ids:

        try:

            task_id = int(item.strip())

        except ValueError:

            continue

        task = find_task(tasks, task_id)

        if task and not task["completed"]:

            task["completed"] = True
            completed_count += 1

    save_tasks(tasks)

    print(
        f"{completed_count} task(s) completed."
    )


# ==========================================
# NEW FEATURE: CATEGORY SUMMARY
# ==========================================

def category_summary(tasks):

    print("\n========== CATEGORY SUMMARY ==========")

    categories = {}

    for task in tasks:

        category = task["category"]

        if category not in categories:

            categories[category] = {
                "total": 0,
                "completed": 0,
                "pending": 0
            }

        categories[category]["total"] += 1

        if task["completed"]:

            categories[category]["completed"] += 1

        else:

            categories[category]["pending"] += 1

    if not categories:

        print("No categories available.")
        return

    for category, data in categories.items():

        print(f"\nCategory: {category}")

        print(
            f"Total: {data['total']}"
        )

        print(
            f"Completed: {data['completed']}"
        )

        print(
            f"Pending: {data['pending']}"
        )


# ==========================================
# NEW FEATURE: PRODUCTIVITY SCORE
# ==========================================

def productivity_score(tasks):

    print("\n========== PRODUCTIVITY SCORE ==========")

    if not tasks:

        print("No tasks available.")
        return

    completed = sum(
        1 for task in tasks
        if task["completed"]
    )

    total = len(tasks)

    score = (
        completed / total
    ) * 100

    print(
        f"\nYour productivity score is: "
        f"{score:.1f}%"
    )

    if score >= 90:

        print(
            "Excellent! You are completing almost "
            "all of your tasks."
        )

    elif score >= 70:

        print(
            "Good job! You are making strong progress."
        )

    elif score >= 50:

        print(
            "You are halfway there. Keep working "
            "through your pending tasks."
        )

    else:

        print(
            "You have many unfinished tasks. "
            "Try focusing on your highest-priority tasks."
        )


# ==========================================
# NEW FEATURE: WEEKLY REPORT
# ==========================================

def weekly_report(tasks):

    print("\n========== WEEKLY PRODUCTIVITY REPORT ==========")

    today = date.today()

    week_start = today - timedelta(
        days=today.weekday()
    )

    week_end = week_start + timedelta(days=6)

    print(
        f"\nWeek: {week_start} to {week_end}"
    )

    created_this_week = 0
    completed_this_week = 0

    for task in tasks:

        created_at = task.get(
            "created_at",
            ""
        )

        try:

            created_date = datetime.strptime(
                created_at,
                "%Y-%m-%d %H:%M"
            ).date()

            if week_start <= created_date <= week_end:

                created_this_week += 1

        except ValueError:

            pass

        if task["completed"]:

            completed_this_week += 1

    print(
        f"\nTasks Created This Week: "
        f"{created_this_week}"
    )

    print(
        f"Completed Tasks: "
        f"{completed_this_week}"
    )

    pending = sum(
        1 for task in tasks
        if not task["completed"]
    )

    print(
        f"Current Pending Tasks: {pending}"
    )


# ==========================================
# NEW FEATURE: ARCHIVE COMPLETED TASKS
# ==========================================

def archive_completed(tasks):

    print("\n========== ARCHIVE COMPLETED TASKS ==========")

    completed = [
        task for task in tasks
        if task["completed"]
    ]

    if not completed:

        print("There are no completed tasks.")
        return

    try:

        with open(
            ARCHIVE_FILE,
            "r"
        ) as file:

            archived = json.load(file)

    except FileNotFoundError:

        archived = []

    except json.JSONDecodeError:

        archived = []

    archived.extend(completed)

    tasks[:] = [
        task for task in tasks
        if not task["completed"]
    ]

    with open(
        ARCHIVE_FILE,
        "w"
    ) as file:

        json.dump(
            archived,
            file,
            indent=4
        )

    save_tasks(tasks)

    print(
        f"{len(completed)} completed task(s) "
        "archived."
    )


# ==========================================
# NEW FEATURE: VIEW ARCHIVED TASKS
# ==========================================

def view_archived_tasks():

    print("\n========== ARCHIVED TASKS ==========")

    try:

        with open(
            ARCHIVE_FILE,
            "r"
        ) as file:

            archived = json.load(file)

    except FileNotFoundError:

        archived = []

    except json.JSONDecodeError:

        archived = []

    if not archived:

        print("No archived tasks.")
        return

    for task in archived:

        display_task(task)

        print("-" * 35)


# ==========================================
# NEW FEATURE: FOCUS TASK
# ==========================================

def set_focus_task(tasks):

    print("\n========== SET FOCUS TASK ==========")

    try:

        task_id = int(
            input("Enter task ID: ")
        )

    except ValueError:

        print("Invalid task ID.")
        return

    task = find_task(tasks, task_id)

    if task is None:

        print("Task not found.")
        return

    for current_task in tasks:

        current_task["focus"] = False

    task["focus"] = True

    save_tasks(tasks)

    print(
        f"'{task['title']}' is now your focus task."
    )


# ==========================================
# NEW FEATURE: VIEW FOCUS TASK
# ==========================================

def view_focus_task(tasks):

    print("\n========== CURRENT FOCUS TASK ==========")

    for task in tasks:

        if task.get("focus", False):

            display_task(task)
            return

    print("You do not have a focus task.")


# ==========================================
# NEW FEATURE: REMOVE FOCUS TASK
# ==========================================

def remove_focus_task(tasks):

    found = False

    for task in tasks:

        if task.get("focus", False):

            task["focus"] = False
            found = True

    if found:

        save_tasks(tasks)

        print("Focus task removed.")

    else:

        print("No focus task is currently set.")


# ==========================================
# NEW FEATURE: DELETE ALL TASKS
# ==========================================

def delete_all_tasks(tasks):

    print("\n========== DELETE ALL TASKS ==========")

    if not tasks:

        print("There are no tasks.")
        return

    print(
        f"You currently have {len(tasks)} task(s)."
    )

    confirmation = input(
        "Type DELETE to confirm: "
    )

    if confirmation == "DELETE":

        tasks.clear()

        save_tasks(tasks)

        print("All tasks deleted.")

    else:

        print("Operation cancelled.")


# ==========================================
# NEW FEATURE: POMODORO TIMER
# ==========================================

def pomodoro_timer():

    print("\n========== POMODORO TIMER ==========")

    print("1. 25 minute focus")
    print("2. 15 minute focus")
    print("3. Custom timer")

    choice = input(
        "Choose timer: "
    )

    if choice == "1":

        minutes = 25

    elif choice == "2":

        minutes = 15

    elif choice == "3":

        try:

            minutes = int(
                input("Minutes: ")
            )

        except ValueError:

            print("Invalid number.")
            return

        if minutes <= 0:

            print("Minutes must be greater than 0.")
            return

    else:

        print("Invalid option.")
        return

    seconds = minutes * 60

    print(
        f"\nFocus session started for "
        f"{minutes} minute(s)."
    )

    print(
        "Press Ctrl+C if you need to stop the timer."
    )

    try:

        while seconds > 0:

            mins = seconds // 60
            secs = seconds % 60

            print(
                f"\rTime Remaining: "
                f"{mins:02d}:{secs:02d}",
                end=""
            )

            time.sleep(1)

            seconds -= 1

        print(
            "\n\nFocus session complete!"
        )

    except KeyboardInterrupt:

        print(
            "\n\nTimer stopped."
        )


# ==========================================
# NEW FEATURE: PRODUCTIVITY MENU
# ==========================================

def productivity_menu(tasks):

    while True:

        print("\n")
        print("=" * 45)
        print("          PRODUCTIVITY CENTER")
        print("=" * 45)

        print("1. Dashboard")
        print("2. Today's Tasks")
        print("3. Overdue Tasks")
        print("4. Upcoming Tasks")
        print("5. Productivity Score")
        print("6. Weekly Report")
        print("7. Category Summary")
        print("8. Pomodoro Timer")
        print("9. Back")

        print("=" * 45)

        choice = input(
            "Choose an option: "
        ).strip()

        if choice == "1":

            productivity_dashboard(tasks)

        elif choice == "2":

            todays_tasks(tasks)

        elif choice == "3":

            overdue_tasks(tasks)

        elif choice == "4":

            upcoming_tasks(tasks)

        elif choice == "5":

            productivity_score(tasks)

        elif choice == "6":

            weekly_report(tasks)

        elif choice == "7":

            category_summary(tasks)

        elif choice == "8":

            pomodoro_timer()

        elif choice == "9":

            break

        else:

            print("Invalid option.")


# ==========================================
# NEW FEATURE: TASK TOOLS MENU
# ==========================================

def task_tools_menu(tasks):

    while True:

        print("\n")
        print("=" * 45)
        print("              TASK TOOLS")
        print("=" * 45)

        print("1. Add Task Note")
        print("2. View Task Notes")
        print("3. Duplicate Task")
        print("4. Complete Multiple Tasks")
        print("5. Set Focus Task")
        print("6. View Focus Task")
        print("7. Remove Focus Task")
        print("8. Archive Completed Tasks")
        print("9. View Archived Tasks")
        print("10. Delete All Tasks")
        print("11. Back")

        print("=" * 45)

        choice = input(
            "Choose an option: "
        ).strip()

        if choice == "1":

            add_task_note(tasks)

        elif choice == "2":

            view_task_notes(tasks)

        elif choice == "3":

            duplicate_task(tasks)

        elif choice == "4":

            quick_complete(tasks)

        elif choice == "5":

            set_focus_task(tasks)

        elif choice == "6":

            view_focus_task(tasks)

        elif choice == "7":

            remove_focus_task(tasks)

        elif choice == "8":

            archive_completed(tasks)

        elif choice == "9":

            view_archived_tasks()

        elif choice == "10":

            delete_all_tasks(tasks)

        elif choice == "11":

            break

        else:

            print("Invalid option.")


# ==========================================
# MAIN MENU
# ==========================================

def main():

    tasks = load_tasks()

    while True:

        print("\n")
        print("=" * 45)
        print("              TO-DO LIST")
        print("=" * 45)

        print("1.  View All Tasks")
        print("2.  Add Task")
        print("3.  Edit Task")
        print("4.  Complete / Uncomplete Task")
        print("5.  Delete Task")
        print("6.  Search Tasks")
        print("7.  Filter Tasks")
        print("8.  Sort Tasks")
        print("9.  Task Statistics")
        print("10. Clear Completed Tasks")
        print("11. Productivity Center")
        print("12. Task Tools")
        print("13. Exit")

        print("=" * 45)

        choice = input(
            "Choose an option: "
        ).strip()

        if choice == "1":
            view_tasks(tasks)

        elif choice == "2":
            add_task(tasks)

        elif choice == "3":
            edit_task(tasks)

        elif choice == "4":
            toggle_task(tasks)

        elif choice == "5":
            delete_task(tasks)

        elif choice == "6":
            search_tasks(tasks)

        elif choice == "7":
            filter_tasks(tasks)

        elif choice == "8":
            sort_tasks(tasks)

        elif choice == "9":
            show_statistics(tasks)

        elif choice == "10":
            clear_completed(tasks)

        elif choice == "11":
            productivity_menu(tasks)

        elif choice == "12":
            task_tools_menu(tasks)

        elif choice == "13":

            save_tasks(tasks)

            print("\nTasks saved successfully.")
            print("Thank you for using the To-Do List.")

            break

        else:

            print(
                "\nInvalid choice. "
                "Please select 1-13."
            )


# ==========================================
# PROGRAM START
# ==========================================

if __name__ == "__main__":
    main()
