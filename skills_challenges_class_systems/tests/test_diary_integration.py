from ..lib.DiaryEntry import DiaryEntry
from ..lib.Diary import Diary
import pytest


def test_add_one_diary_entry():
    my_diary = Diary()
    entry_1 = DiaryEntry("My Title", "These are the contents of my diary entry...")
    my_diary.add(entry_1)
    assert my_diary.entries == [entry_1]


def test_add_multiple_entries():
    my_diary = Diary()
    entry_1 = DiaryEntry("My Title", "These are the contents of my diary entry...")
    entry_2 = DiaryEntry(
        "My Sequel", "These are the contents of my second diary entry."
    )
    my_diary.add(entry_1)
    my_diary.add(entry_2)
    assert my_diary.entries == [entry_1, entry_2]


def test_display_all():
    my_diary = Diary()
    entry_1 = DiaryEntry("My Title", "These are the contents of my diary entry...")
    entry_2 = DiaryEntry(
        "My Sequel", "These are the contents of my second diary entry."
    )
    my_diary.add(entry_1)
    my_diary.add(entry_2)
    assert my_diary.all() == [entry_1, entry_2]


def test_no_entries_when_calling_all():
    my_diary = Diary()
    assert my_diary.all() == "There are no entries in this diary"


def test_count_words():
    my_diary = Diary()
    entry_1 = DiaryEntry("My Title", "These are the contents of my diary entry...")
    entry_2 = DiaryEntry(
        "My Sequel", "These are the contents of my second diary entry."
    )
    my_diary.add(entry_1)
    my_diary.add(entry_2)
    assert my_diary.count_words() == 17


def test_count_words_with_no_entries():
    my_diary = Diary()
    assert my_diary.count_words() == 0


def test_reading_time():
    my_diary = Diary()
    entry_1 = DiaryEntry("My Title", "These are the contents of my diary entry...")
    entry_2 = DiaryEntry(
        "My Sequel", "These are the contents of my second diary entry."
    )
    my_diary.add(entry_1)
    my_diary.add(entry_2)
    assert my_diary.reading_time(17) == 1


def test_reading_time_rounding():
    my_diary = Diary()
    entry_1 = DiaryEntry("My Title", "These are the contents of my diary entry...")
    entry_2 = DiaryEntry(
        "My Sequel", "These are the contents of my second diary entry."
    )
    my_diary.add(entry_1)
    my_diary.add(entry_2)
    assert my_diary.reading_time(8) == 2
    assert my_diary.reading_time(10) == 2
    assert my_diary.reading_time(100) == 1


def test_reading_time_with_no_entries():
    my_diary = Diary()
    with pytest.raises(Exception) as e:
        assert my_diary.reading_time(8)
    error_message = str(e.value)
    assert error_message == "Cannot calculate reading time without any entries"


def test_find_best_entry_one_entry():
    my_diary = Diary()
    entry_1 = DiaryEntry("My Title", "These are the contents of my diary entry...")
    my_diary.add(entry_1)
    assert my_diary.find_best_entry_for_reading_time(20, 50) == entry_1


def test_find_best_entry_two_entries():
    my_diary = Diary()
    entry_1 = DiaryEntry("My Title", "These are the contents of my diary entry...")
    entry_2 = DiaryEntry(
        "My Sequel",
        "These are the contents of my second diary entry. This entry has more words than entry one",
    )
    my_diary.add(entry_1)
    my_diary.add(entry_2)
    assert my_diary.find_best_entry_for_reading_time(20, 50) == entry_2


def test_find_best_entry_two_entries_swapped():
    my_diary = Diary()
    entry_2 = DiaryEntry(
        "My Sequel",
        "These are the contents of my second diary entry. This entry has more words than entry one",
    )
    entry_1 = DiaryEntry("My Title", "These are the contents of my diary entry...")
    my_diary.add(entry_2)
    my_diary.add(entry_1)
    assert my_diary.find_best_entry_for_reading_time(20, 50) == entry_2


def test_find_best_entry_multiple_entries():
    my_diary = Diary()
    entry_1 = DiaryEntry("My Title", "These are the contents of my diary entry...")
    entry_2 = DiaryEntry(
        "Longest Entry",
        "These are the contents of my diary entry. This entry has more words than every other entry in my diary",
    )
    entry_3 = DiaryEntry("Short Entry", "Entry contents here")
    entry_4 = DiaryEntry("Another Entry", "Another entry added to the diary")
    my_diary.add(entry_1)
    my_diary.add(entry_2)
    my_diary.add(entry_3)
    my_diary.add(entry_4)
    assert my_diary.find_best_entry_for_reading_time(20, 50) == entry_2


def test_find_best_entry_short_reading_time():
    my_diary = Diary()
    entry_1 = DiaryEntry("My Title", "These are the contents of my diary entry...")
    entry_2 = DiaryEntry(
        "Longest Entry",
        "These are the contents of my diary entry. This entry has more words than every other entry in my diary",
    )
    entry_3 = DiaryEntry("Short Entry", "Entry contents here")
    entry_4 = DiaryEntry("Another Entry", "Another entry added to the diary")
    my_diary.add(entry_1)
    my_diary.add(entry_2)
    my_diary.add(entry_3)
    my_diary.add(entry_4)
    assert (
        my_diary.find_best_entry_for_reading_time(1, 2)
        == "There are no entries short enough for you to read"
    )


def test_find_best_entry_with_no_entries():
    my_diary = Diary()
    with pytest.raises(Exception) as e:
        assert my_diary.find_best_entry_for_reading_time(10, 20)
    error_message = str(e.value)
    assert error_message == "Cannot find entry to read without any entries"
