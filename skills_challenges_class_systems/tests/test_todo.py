from ..lib.Todo import Todo
import pytest


class TestTodo:
    def test_task_added_correctly(self):
        todo = Todo("Walk the dog")
        assert todo.task == "Walk the dog"
        assert todo.complete == False

    def test_task_as_empty_string(self):
        with pytest.raises(Exception, match="No task provided"):
            todo = Todo("")

    def test_task_is_marked_complete(self):
        todo = Todo("Walk the dog")
        todo.mark_complete()
        assert todo.complete == True

    def test_task_is_already_complete(self):
        todo = Todo("Walk the dog")
        todo.mark_complete()
        with pytest.raises(Exception, match="Task is already complete"):
            todo.mark_complete()
