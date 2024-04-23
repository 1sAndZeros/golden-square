# TaskTracker Class Design Recipe

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
class TaskTracker:
    # User-facing properties:
    #   tasks: list[string]

    def __init__(self):
        # Side effects:
        #   Sets the tasks property of the self object
        pass # No code here yet

    def add(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   adds the task to the self object
        pass # No code here yet

    def mark_complete(self, task_to_remove):
        # Returns:
        #   Nothing
        # Side-effects:
        #   removes the given task from the self object
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
"""
Given a name and a task
#remind reminds the user to do the task
"""
tracker = TaskTracker()
tracker.add("Walk the dog")
tracker.tasks # => ["Walk the dog"]
tracker.add("Go food shopping")
tracker.tasks # => ["Walk the dog", "Go food shopping"]

"""
Given a name of task
#mark_complete removes the task from the list
"""
tracker = TaskTracker()
tracker.add("Walk the dog")
tracker.add("Go food shopping")
tracker.mark_complete("Walk the dog")
tracker.tasks # => ["Go food shopping"]

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
