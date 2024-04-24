from ..lib.DiaryEntry import DiaryEntry


class TestDiaryEntry:
    def test_diary_entry_initialised(self):
        entry1 = DiaryEntry("Entry One", "This is a diary entry")
        assert entry1.title == "Entry One"
        assert entry1.contents == "This is a diary entry"

    def test_entry_count_words(self):
        entry1 = DiaryEntry("Entry One", "This is a diary entry")
        assert entry1.count_words() == 5

    def test_get_phone_no(self):
        entry1 = DiaryEntry(
            "Entry One", "This is my first diary entry. I called John on 12345678910"
        )
        assert entry1.get_phone_no() == "12345678910"

    def test_no_phone_numbers(self):
        entry1 = DiaryEntry("Entry One", "This is my first diary entry. I called John.")
        assert entry1.get_phone_no() == None
