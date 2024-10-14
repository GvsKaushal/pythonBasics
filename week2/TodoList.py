import sys
from todo import TodoApp


def main():
    app = TodoApp()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Update Task")
        print("6. Quit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            task = input("Enter task: ").strip()
            app.add_task(task)
        elif choice == '2':
            app.list_tasks()
        elif choice == '3':
            app.list_tasks()
            try:
                task_num = int(input("Enter task number to mark as done: "))
                app.mark_done(task_num)
            except ValueError:
                print("Invalid input! Please enter a number.")
        elif choice == '4':
            app.list_tasks()
            try:
                task_num = int(input("Enter task number to delete: "))
                app.delete_task(task_num)
            except ValueError:
                print("Invalid input! Please enter a number.")
        elif choice == '5':
            app.list_tasks()
            try:
                task_num = int(input("Enter task number to update: "))
                new_task = input("Enter new task description: ").strip()
                app.update_task(task_num, new_task)
            except ValueError:
                print("Invalid input! Please enter a number.")
        elif choice == '6':
            app.save_tasks()
            print("Changes saved")
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice, please try again.")


if __name__ == '__main__':
    main()
