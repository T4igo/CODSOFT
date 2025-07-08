
todo_list = []

def display_menu():
    print("\n===== Welcome to Your To-Do List =====")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Remove a task")
    print("4. Exit the application")

def add_task():
    task = input(" What task would you like to add? ")
    if task.strip():
        todo_list.append(task.strip())
        print(f" Great! '{task}' has been added to your list.")
    else:
        print(" Task cannot be empty. Try again.")

def view_tasks():
    if not todo_list:
        print(" Your to-do list is currently empty.")
    else:
        print("\n Here are your current tasks:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def remove_task():
    view_tasks()
    if todo_list:
        try:
            index = int(input(" Enter the number of the task to remove: "))
            if 1 <= index <= len(todo_list):
                removed_task = todo_list.pop(index - 1)
                print(f" '{removed_task}' has been removed from your list.")
            else:
                print(" That number doesn't match any task.")
        except ValueError:
            print(" Please enter a valid number.")

def main():
    while True:
        display_menu()
        choice = input(" Choose an option (1-4): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print(" Thanks for using the To-Do List. Stay productive!")
            break
        else:
            print(" Invalid option. Please select from 1 to 4.")

if __name__ == "__main__":
    main()
