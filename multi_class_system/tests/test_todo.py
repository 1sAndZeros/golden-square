from ..lib.Todo import Todo


class TestTodo:
    def test_todo_initialised(self):
        task1 = Todo("Go Shopping")
        task1.task == "Go Shopping"
        assert task1.complete == False

    def test_mark_complete(self):
        task1 = Todo("Go Shopping")
        task1.mark_complete()
        assert task1.complete == True
