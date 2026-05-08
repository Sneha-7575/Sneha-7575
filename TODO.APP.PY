tasks = []

while True:
    print("\n--- TO-DO APP ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    
    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added!")

    
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            task_num = int(input("Enter task number to remove: "))

            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")

    
    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
