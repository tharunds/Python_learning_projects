def add_task(tasks):
    title = input("Enter task title: ")
    category = input("Enter category (e.g., Work, Personal, Shopping): ")
    
    # Create a task dictionary
    task = {
        "title": title,
        "category": category,
        "completed": False
    }
    tasks.append(task)
    print(f"Task '{title}' added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!")
        return
        
    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "✅" if task["completed"] else "❌"
        print(f"{index}. [{status}] {task['title']} ({task['category']})")


def mark_complete(tasks):
    view_tasks(tasks)
    if not tasks: return
    
    try:
        idx = int(input("Enter the task number to mark complete: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["completed"] = True
            print(f"Marked '{tasks[idx]['title']}' as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks: return
    
    try:
        idx = int(input("Enter the task number to delete: ")) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            print(f"Deleted task: '{removed['title']}'")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
def main_menu():
    tasks = [] # This will hold our task dictionaries
    
    while True:
        print("\n--- TO-DO MANAGER ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == "1":
            view_tasks(tasks)
            # Function placeholder
        elif choice == "2":
            add_task(tasks)
            # Function placeholder
        elif choice == "3":
            pass # We will add functionality here later
        elif choice == "4":
            pass # We will add functionality here later
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

# fun to add tasks


