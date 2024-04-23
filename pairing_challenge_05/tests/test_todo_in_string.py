from ..lib.todo_in_string import todo_in_string


def test_todo_in_string():
    chore = todo_in_string("#TODO go to the gym")
    expected = True
    assert chore == expected


def test_todo_not_in_string():
    chore = todo_in_string("#TO go to the gym")
    expected = False
    assert chore == expected


def test_todo_lower_in_string():
    chore = todo_in_string("#todo go to the gym")
    expected = False
    assert chore == expected
