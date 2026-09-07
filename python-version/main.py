import json
from datetime import datetime

FILE_NAME = "tasks.json"


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
        print("11. Exit")

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

            save_tasks(tasks)

            print("\nTasks saved successfully.")
            print("Thank you for using the To-Do List.")
            break

        else:

            print(
                "\nInvalid choice. "
                "Please select 1-11."
            )


# ==========================================
# PROGRAM START
# ==========================================

if __name__ == "__main__":
    main()
