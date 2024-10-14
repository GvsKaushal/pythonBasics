class TodoApp:
    def __init__(self, filename='tasks.txt'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        tasks = []
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    task, status = line.strip().split(' | ')
                    tasks.append({'task': task, 'done': status == 'Done'})
        except FileNotFoundError:
            pass
        return tasks

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            for task in self.tasks:
                status = "Done" if task['done'] else "Not Done"
                file.write(f"{task['task']} | {status}\n")

    def add_task(self, task):
        if not task:
            print("Task cannot be empty.")
            return
        self.tasks.append({'task': task, 'done': False})
        print(f"Added task: {task}")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return

        print("Your tasks:")
        print("--------------------------------------------------------------------")
        for idx, task in enumerate(self.tasks, start=1):
            status = "Done" if task['done'] else "Not Done"
            print(f"{idx}. {task['task']} [{status}]")
        print("--------------------------------------------------------------------")

    def mark_done(self, task_number):
        try:
            self.tasks[task_number - 1]['done'] = True
            print(f"Marked task {task_number} as done.")
        except IndexError:
            print(f"Task {task_number} doesn't exist.")

    def delete_task(self, task_number):
        try:
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Deleted task: {removed_task['task']}")
        except IndexError:
            print(f"Task {task_number} doesn't exist.")

    def update_task(self, task_number, new_task):
        try:
            if not new_task:
                print("Task cannot be empty.")
                return
            old_task = self.tasks[task_number - 1]['task']
            self.tasks[task_number - 1]['task'] = new_task
            print(f"Updated task {task_number} from '{old_task}' to '{new_task}'")
        except IndexError:
            print(f"Task {task_number} doesn't exist.")
