from lib.most_often import MostOften

def test_initialises_correctly():
    most_often = MostOften(["Apple", "Banana", "Pear", "Pear"])
    assert most_often.starting_list == ["Apple", "Banana", "Pear", "Pear"]

def test_add_new_item():
    most_often = MostOften(["Apple", "Banana", "Pear", "Pear"])
    most_often.add_new("Strawberry")
    assert most_often.starting_list == ["Apple", "Banana", "Pear", "Pear", "Strawberry"]

def test_get_most_often_where_there_is_a_clear_winner():
    most_often = MostOften(["Apple", "Banana", "Pear", "Pear"])
    assert most_often.get_most_often() == "Pear"

def test_get_most_often_where_there_is_no_winner():
    most_often = MostOften(["Apple", "Banana", "Pear"])
    assert most_often.get_most_often() == "no clear winner"

def test_get_most_often_where_clear_winner_has_been_added():
    most_often = MostOften(["Apple", "Banana", "Pear"])
    most_often.add_new("Banana")
    assert most_often.get_most_often() == "Banana"

def test_get_most_often_where_list_is_empty():
    most_often = MostOften([])
    assert most_often.get_most_often() == "no clear winner"