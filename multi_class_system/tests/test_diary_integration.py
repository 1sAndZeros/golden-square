from ..lib.Diary import *
from ..lib.DiaryEntry import *
import pytest


def test_entry_added_to_diary():
    my_diary = Diary()
    entry1 = DiaryEntry("Entry One", "This is my first diary entry")
    my_diary.add(entry1)
    assert my_diary.entries == [entry1]


def test_add_two_entries():
    my_diary = Diary()
    entry1 = DiaryEntry("Entry One", "This is my first diary entry")
    my_diary.add(entry1)
    entry2 = DiaryEntry("Entry Two", "This is my second diary entry")
    my_diary.add(entry2)
    assert my_diary.entries == [entry1, entry2]


def test_read_entry():
    my_diary = Diary()
    entry1 = DiaryEntry("Entry One", "This is my first diary entry")
    my_diary.add(entry1)
    entry2 = DiaryEntry("Entry Two", "This is my second diary entry")
    my_diary.add(entry2)
    assert my_diary.read_entry("Entry Two") == "This is my second diary entry"


def test_wrong_title_raises_error():
    my_diary = Diary()
    entry1 = DiaryEntry("Entry One", "This is my first diary entry")
    my_diary.add(entry1)
    entry2 = DiaryEntry("Entry Two", "This is my second diary entry")
    my_diary.add(entry2)
    with pytest.raises(Exception) as e:
        my_diary.read_entry("Entry Three")
    error_message = str(e.value)
    assert error_message == "This diary entry doesn't exist"


def test_read_entry_given_time():
    my_diary = Diary()
    entry1 = DiaryEntry("Entry One", "This is my first diary entry")
    my_diary.add(entry1)
    entry2 = DiaryEntry("Entry Two", "This is my second diary entry which is longer")
    my_diary.add(entry2)
    assert my_diary.read_entry_given_time(2, 4) == "This is my first diary entry"
    assert (
        my_diary.read_entry_given_time(10, 20)
        == "This is my second diary entry which is longer"
    )


def test_no_entries_to_read():
    my_diary = Diary()
    entry1 = DiaryEntry("Entry One", "This is my first diary entry")
    my_diary.add(entry1)
    entry2 = DiaryEntry("Entry Two", "This is my second diary entry which is longer")
    my_diary.add(entry2)
    assert (
        my_diary.read_entry_given_time(2, 2)
        == "There are no entries to read in the time given"
    )


def test_get_contacts():
    my_diary = Diary()
    entry1 = DiaryEntry(
        "Entry One", "This is my first diary entry. I called John on 12345678910"
    )
    my_diary.add(entry1)
    entry2 = DiaryEntry(
        "Entry Two",
        "This is my second diary entry which is longer. I called Sarahs number which is 10987654321. We had a nice catch up",
    )
    my_diary.add(entry2)
    assert my_diary.get_contacts() == ["12345678910", "10987654321"]


def test_no_contacts():
    my_diary = Diary()
    entry1 = DiaryEntry("Entry One", "This is my first diary entry")
    my_diary.add(entry1)
    entry2 = DiaryEntry(
        "Entry Two",
        "This is my second diary entry which is longer. I called Sarah and we had a nice catch up",
    )
    my_diary.add(entry2)
    assert my_diary.get_contacts() == "No contacts exist"
