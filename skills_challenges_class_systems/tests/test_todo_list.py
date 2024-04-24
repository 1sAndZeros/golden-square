from ..lib.TodoList import TodoList


class TestTodo:
    def test_list_initialises_correclty(self):
        todoList = TodoList()
        assert todoList.todos == []

    def test_incomplete_returns_empty_list(self):
        todoList = TodoList()
        assert todoList.incomplete() == []

    def test_complete_returns_empty_list(self):
        todoList = TodoList()
        assert todoList.complete() == []
