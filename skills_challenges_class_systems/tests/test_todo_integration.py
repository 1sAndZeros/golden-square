from ..lib.Todo import Todo
from ..lib.TodoList import TodoList


class TestTodoIntegration:
    def test_todo_is_added_to_todods(self):
        todoList = TodoList()
        todo = Todo("Go Shopping")
        todo2 = Todo("Beat 5km PB")
        todoList.add(todo)
        assert todoList.todos == [todo]
        todoList.add(todo2)
        assert todoList.todos == [todo, todo2]

    def test_incomplete_returns_all_incomplete_todos(self):
        todoList = TodoList()
        todo = Todo("Go Shopping")
        todo2 = Todo("Beat 5km PB")
        todoList.add(todo)
        todoList.add(todo2)
        assert todoList.incomplete() == [todo, todo2]
        todo.mark_complete()
        assert todoList.incomplete() == [todo2]

    def test_complete_returns_all_complete_todos(self):
        todoList = TodoList()
        todo = Todo("Go Shopping")
        todo2 = Todo("Beat 5km PB")
        todoList.add(todo)
        todoList.add(todo2)
        assert todoList.complete() == []
        todo.mark_complete()
        assert todoList.complete() == [todo]
        todo2.mark_complete()
        assert todoList.complete() == [todo, todo2]

    def test_give_up_marks_all_tasks_complete(self):
        todoList = TodoList()
        todo = Todo("Go Shopping")
        todo2 = Todo("Beat 5km PB")
        todoList.add(todo)
        todoList.add(todo2)
        todoList.give_up()
        assert todoList.complete() == [todo, todo2]
