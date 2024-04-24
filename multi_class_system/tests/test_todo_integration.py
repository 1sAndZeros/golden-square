from ..lib.TodoList import TodoList
from ..lib.Todo import Todo


def test_todo_added():
    my_todo_list = TodoList()
    task1 = Todo("Make a shopping list")
    my_todo_list.add(task1)
    assert my_todo_list.todos == [task1]
    task2 = Todo("Buy the shopping")
    my_todo_list.add(task2)
    assert my_todo_list.todos == [task1, task2]
