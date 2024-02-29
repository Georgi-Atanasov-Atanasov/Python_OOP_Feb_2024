from project.task import Task


class Section:

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task: Task):
        if task not in self.tasks:
            self.tasks.append(task)
            return f"Task {task.details()} is added to the section"
        else:
            return f"Task is already in the section {self.name}"

    def complete_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"
        # try:
        #     task = next(filter(lambda t: t.name == task_name, self.tasks))
        # except StopIteration:
        #     return f"Could not find task with the name {task_name}"
        #
        # task.completed = True
        #
        # return f"Completed task {task_name}"

    def clean_section(self):
        cleaned_tasks = 0
        for task in self.tasks:
            if task.completed == True:
                self.tasks.remove(task)
                cleaned_tasks += 1
        return f"Cleared {cleaned_tasks} tasks."

    def view_section(self):
        show_tasks_format = '\n'.join([task.details() for task in self.tasks])
        return f"Section {self.name}:\n{show_tasks_format}"