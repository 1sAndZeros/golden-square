from ..lib.Diary import Diary
from ..lib.TodoList import TodoList
from ..lib.Person import Person


def test_user_initialised():
    johns_diary = Diary()
    johns_todo_list = TodoList()
    john_smith = Person("John Smith", diary=johns_diary, todo_list=johns_todo_list)
    assert john_smith.name == "John Smith"
    assert john_smith.diary == johns_diary
    assert john_smith.todo_list == johns_todo_list
