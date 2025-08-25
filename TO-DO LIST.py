todo_list = []

while True:
    print("\n   TO-DO LIST MENU  ")
    print("1. Add task")
    print("2. View all tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Enter your choice(1-4): ")

    if choice == "1":
        task = input("Enter the task : ")
        todo_list.append(task)
        print(f"'{task}' has been added.")

    elif choice == "2":
        print("\nYour Tasks:")
        for i, t in enumerate(todo_list, start=1):
            print(f"{i}. {t}")

    elif choice == "3":
        task_n = int(input("Enter the number of the task to remove: "))
        if 1 <= task_n <= len(todo_list):
            removed = todo_list.pop(task_n - 1)
            print(f"'{removed}' Removed.")
        else:
            print("Invalid task number.")

    elif choice == "4":
        print("Exiting")
        break

    else:
        print("Invalid choice.")
