class TaskTracker:
    # User-facing properties:
    #   tasks: list[string]

    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def mark_complete(self, task_to_remove):
        self.tasks = [task for task in self.tasks if task != task_to_remove]
