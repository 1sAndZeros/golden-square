class Todo:
    # User-facing properties:
    #   task: name of the task
    #   complete: decribes whether the task is complete

    def __init__(self, task):
        # Parameters:
        #   task: name of the task
        self.task = task
        self.complete = False

    def mark_complete(self):
        self.complete = True
