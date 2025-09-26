FILENAME = "tasks.txt"

def load_tasks():
    tasks = []
    try:
        with open(FILENAME, "r") as f:
            for line in f:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass
    return tasks

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def menu():
    print("\n--- TO-DO LIST ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def main():
    tasks = load_tasks()

    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == "1":
            print("\nYour Tasks:")
            if not tasks:
                print("No tasks yet!")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")

        elif choice == "2":
            task = input("Enter new task: ").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
                print("Task added.")
            else:
                print("Task cannot be empty!")

        elif choice == "3":
            if not tasks:
                print("No tasks to remove.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                try:
                    idx = int(input("Enter task number to remove: "))
                    if 1 <= idx <= len(tasks):
                        removed = tasks.pop(idx - 1)
                        save_tasks(tasks)
                        print(f"Removed: {removed}")
                    else:
                        print("Invalid number!")
                except ValueError:
                    print("Enter a valid number!")

        elif choice == "4":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid option, try again!")

if __name__ == "__main__":
    main()
