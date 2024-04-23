from ..lib.TaskTracker import TaskTracker


class TestTaskTracker:

    def test_instance_initialises(self):
        tracker = TaskTracker()
        assert tracker.tasks == []

    def test_add_method(self):
        """
        Given a name and a task\n
        #remind reminds the user to do the task
        """

        tracker = TaskTracker()
        tracker.add("Walk the dog")
        assert tracker.tasks == ["Walk the dog"]
        tracker.add("Go food shopping")
        assert tracker.tasks == ["Walk the dog", "Go food shopping"]

    def test_mark_complete_method(self):
        """
        Given a name of task\n
        #mark_complete removes the task from the list
        """
        tracker = TaskTracker()
        tracker.add("Walk the dog")
        tracker.add("Go food shopping")
        tracker.mark_complete("Walk the dog")
        assert tracker.tasks == ["Go food shopping"]
