class TodoApp:
    def __init__(self, filename='tasks.txt'):
        self.__filename = filename
        self.__tasks = self.load_tasks()

    def load_tasks(self):
        __tasks = []
        try:
            with open(self.__filename, 'r') as file:
                for line in file:
                    task, status = line.strip().split(' | ')
                    __tasks.append({'task': task, 'done': status == 'Done'})
        except FileNotFoundError:
            pass
        return __tasks

    def save_tasks(self):
        with open(self.__filename, 'w') as file:
            for task in self.__tasks:
                status = "Done" if task['done'] else "Not Done"
                file.write(f"{task['task']} | {status}\n")

    def add_task(self, task):
        if not task:
            print("Task cannot be empty.")
            return
        self.__tasks.append({'task': task, 'done': False})
        print(f"Added task: {task}")

    def list_tasks(self):
        if not self.__tasks:
            print("No tasks in the list.")
            return

        print("Your tasks:")
        print("--------------------------------------------------------------------")
        for idx, task in enumerate(self.__tasks, start=1):
            status = "Done" if task['done'] else "Not Done"
            print(f"{idx}. {task['task']} [{status}]")
        print("--------------------------------------------------------------------")

    def mark_done(self, task_number):
        try:
            self.__tasks[task_number - 1]['done'] = True
            print(f"Marked task {task_number} as done.")
        except IndexError:
            print(f"Task {task_number} doesn't exist.")

    def delete_task(self, task_number):
        try:
            removed_task = self.__tasks.pop(task_number - 1)
            print(f"Deleted task: {removed_task['task']}")
        except IndexError:
            print(f"Task {task_number} doesn't exist.")

    def update_task(self, task_number, new_task):
        try:
            if not new_task:
                print("Task cannot be empty.")
                return
            old_task = self.__tasks[task_number - 1]['task']
            self.__tasks[task_number - 1]['task'] = new_task
            print(f"Updated task {task_number} from '{old_task}' to '{new_task}'")
        except IndexError:
            print(f"Task {task_number} doesn't exist.")
