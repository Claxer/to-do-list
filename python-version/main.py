# ==========================================
# Python To-Do List
# ==========================================

FILE_NAME = "tasks.txt"


# -----------------------------
# Load tasks from file
# -----------------------------
def load_tasks():
    tasks = []

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip()

                if line:
                    parts = line.split("|")

                    task = {
                        "name": parts[0],
                        "completed": parts[1] == "True"
                    }

                    tasks.append(task)

    except FileNotFoundError:
        # File doesn't exist yet
        pass

    return tasks


# -----------------------------
# Save tasks to file
# -----------------------------
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(
                f"{task['name']}|{task['completed']}\n"
            )


# -----------------------------
# Display tasks
# -----------------------------
def view_tasks(tasks):
    print("\n========== YOUR TASKS ==========")

    if not tasks:
        print("You don't have any tasks yet.")
        return

    for index, task in enumerate(tasks, start=1):

        if task["completed"]:
            status = "✓ Completed"
        else:
            status = "○ Pending"

        print(f"{index}. {task['name']} - {status}")


# -----------------------------
# Add a task
# -----------------------------
def add_task(tasks):
    print("\n========== ADD TASK ==========")

    task_name = input("Enter your task: ").strip()

    if not task_name:
        print("Task cannot be empty.")
        return

    tasks.append({
        "name": task_name,
        "completed": False
    })

    save_tasks(tasks)

    print("Task added successfully!")


# -----------------------------
# Complete a task
# -----------------------------
def complete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_number = int(
            input("\nEnter the task number to complete: ")
        )

        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
            return

        task = tasks[task_number - 1]

        if task["completed"]:
            print("This task is already completed.")
        else:
            task["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!")

    except ValueError:
        print("Please enter a valid number.")


# -----------------------------
# Delete a task
# -----------------------------
def delete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_number = int(
            input("\nEnter the task number to delete: ")
        )

        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
            return

        removed_task = tasks.pop(task_number - 1)

        save_tasks(tasks)

        print(
            f"Deleted task: {removed_task['name']}"
        )

    except ValueError:
        print("Please enter a valid number.")


# -----------------------------
# Main program
# -----------------------------
def main():

    tasks = load_tasks()

    while True:

        print("\n")
        print("================================")
        print("          TO-DO LIST")
        print("================================")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        print("================================")

        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)

        elif choice == "2":
            add_task(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            save_tasks(tasks)
            print("\nYour tasks have been saved.")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-5.")


# -----------------------------
# Start program
# -----------------------------
if __name__ == "__main__":
    main()
