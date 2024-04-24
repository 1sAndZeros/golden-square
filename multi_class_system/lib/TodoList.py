class TodoList:
    # User-facing properties:
    #   todos: list of todo items

    def __init__(self):
        # Parameters:
        #   todos: list of todo instances
        self.todos = []

    def add(self, task):
        # Paramters:
        #   string representing description of the task
        self.todos.append(task)
