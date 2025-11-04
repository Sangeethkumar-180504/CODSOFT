# Simple To-Do List Application in Python

# List to store tasks
tasks = []

def show_menu():
    print("\n========== TO-DO LIST MENU ==========")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")
    print("=====================================")

def view_tasks():
    if not tasks:
        print("\nNo tasks found!")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            status = "✅ Done" if task['done'] else "❌ Not Done"
            print(f"{index}. {task['task']}  -->  {status}")

def add_task():
    task_name = input("\nEnter a new task: ").strip()
    if task_name:
        tasks.append({"task": task_name, "done": False})
        print(f"Task '{task_name}' added successfully!")
    else:
        print("Task cannot be empty.")

def mark_done():
    view_tasks()
    try:
        task_num = int(input("\nEnter task number to mark as done: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["done"] = True
            print(f"Task '{tasks[task_num - 1]['task']}' marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("\nEnter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Task '{removed['task']}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# === Main Program Loop ===
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ").strip()

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("\nGoodbye! 👋")
        break
    else:
        print("Invalid choice. Please try again.")
