from ..lib.BirthdayCards import BirthdayCards
import pytest


@pytest.fixture
def birthday_cards():
    return BirthdayCards()


def test_instance_initialises_correctly(birthday_cards):
    assert birthday_cards.friends == []


def test_add_friend(birthday_cards):
    birthday_cards.add_friend("Daisy", "06/09/1990")
    assert birthday_cards.friends == [
        {"name": "Daisy", "dob": "06/09/1990", "card_sent": False}
    ]
    birthday_cards.add_friend("John", "01/02/2000")
    assert birthday_cards.friends == [
        {"name": "Daisy", "dob": "06/09/1990", "card_sent": False},
        {"name": "John", "dob": "01/02/2000", "card_sent": False},
    ]


def test_update_friends_name(birthday_cards):
    birthday_cards.add_friend("John", "01/02/2000")
    birthday_cards.update_friend("John", "Jonathon", "name")
    assert birthday_cards.friends == [
        {"name": "Jonathon", "dob": "01/02/2000", "card_sent": False},
    ]


def test_update_friends_dob(birthday_cards):
    birthday_cards.add_friend("Elizabeth", "21/04/1914")
    birthday_cards.update_friend("Elizabeth", "15/06/1924", "dob")
    assert birthday_cards.friends == [
        {"name": "Elizabeth", "dob": "15/06/1924", "card_sent": False},
    ]


def test_upcoming_birthdays(birthday_cards):
    birthday_cards.add_friend("Elizabeth", "21/05/1914")
    birthday_cards.add_friend("John", "01/07/2000")

    assert birthday_cards.upcoming_birthdays_list() == [
        {"name": "Elizabeth", "dob": "21/05/1914", "card_sent": False}
    ]

    assert birthday_cards.upcoming_birthdays_list(timeframe=180) == [
        {"name": "Elizabeth", "dob": "21/05/1914", "card_sent": False},
        {"name": "John", "dob": "01/07/2000", "card_sent": False},
    ]


def test_upcoming_ages(birthday_cards):
    birthday_cards.add_friend("Elizabeth", "21/05/1914")
    birthday_cards.add_friend("John", "01/07/2000")
    assert birthday_cards.upcoming_ages() == [("Elizabeth", 110)]


def test_mark_as_sent(birthday_cards):
    birthday_cards.add_friend("Elizabeth", "21/05/1914")
    birthday_cards.add_friend("John", "01/07/2000")
    birthday_cards.mark_as_sent("John")
    assert birthday_cards.friends == [
        {"name": "Elizabeth", "dob": "21/05/1914", "card_sent": False},
        {"name": "John", "dob": "01/07/2000", "card_sent": True},
    ]
