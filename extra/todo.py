# To Do List App (CLI).

print("Welcome to the Todo List App!")
print("This app allows you to manage your tasks from the command line.")
print("You can add, view, and delete tasks.")

#Menu
tasks = []
for menu in range(100):
    print("Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    choice = input("Please select an option (1-4): ")
    if choice == '1':
        print("You chose to add a task.")
        # Task Management - Adding Tasks
        print("Insert your task here:")
        task = input()
        print(f"Task {task} added.")
        tasks.append(task)
        print("\n\n")
    elif choice == '2':
        print("You chose to view tasks.")
        # Task Management - Viewing Tasks
        print("Here are your current tasks:")
        if not tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        print("\n\n")
    elif choice == '3':
        print("You chose to delete a task.")
        # Task Management - Deleting Tasks
        print("You can delete a task by entering its number (1-5).")
        if not tasks:
            print("No tasks available to delete.")
        else:
            task_number = int(input("Enter the task number to delete: "))
            if 1 <= task_number <= len(tasks):
                deleted_task = tasks.pop(task_number - 1)
                print(f"Task '{deleted_task}' has been deleted.")
            else:
                print("Invalid task number. No task deleted.")
            print("\n\n")
    elif choice == '4':
        print("Exiting the Todo List App. Goodbye!")
        break

# End of Todo List App


