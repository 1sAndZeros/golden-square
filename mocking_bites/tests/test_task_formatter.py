from ..lib.TaskFormatter import TaskFormatter
from unittest.mock import Mock


class TestTaskFormatter:
    def test_instance_initialises(self):
        task = Mock()
        task_formatter = TaskFormatter(task)
        assert task_formatter.task == task

    def test_format_method_when_task_is_not_complete(self):
        task = Mock()
        task.complete = False
        task.title = "take The dog fOr a wAlK"
        task_formatter = TaskFormatter(task)
        assert task_formatter.format() == "[] Take the dog for a walk"

    def test_format_method_when_task_is_complete(self):
        task = Mock()
        task.complete = True
        task.title = "take The dog fOr a wAlK"
        task_formatter = TaskFormatter(task)
        assert task_formatter.format() == "[x] Take the dog for a walk"
