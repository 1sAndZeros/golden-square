from ..lib.DiaryEntry import DiaryEntry


class TestDiaryEntry:
    def test_instance_initialises_correctly(self):
        entry = DiaryEntry("Day One", "What a day of test driving classes")
        assert entry.title == "Day One"
        assert entry.contents == "What a day of test driving classes"
        assert entry.words_read == 0

    def test_format_methods_formats_correctly(self):
        entry = DiaryEntry("   Day One  ", "   What a day of test driving classes  ")
        assert entry.format() == "Day One: What a day of test driving classes"

    def test_count_words(self):
        entry = DiaryEntry("Day One", "What a day of test driving classes")
        assert entry.count_words() == 7

    def test_reading_time(self):
        entry = DiaryEntry("Day One", "What a day of test driving classes")
        assert entry.reading_time(7) == 1

        entry2 = DiaryEntry("Day Two", "classes " * 200)
        assert entry2.reading_time(100) == 2

    def test_reading_whole_chunk(self):
        entry = DiaryEntry("Day One", "What a day of test driving classes")
        chunk = entry.reading_chunk(2, 5)
        assert chunk == "What a day of test driving classes"

    def test_reading_two_chunks(self):
        entry = DiaryEntry("Day One", "What a day of test driving classes")
        chunk = entry.reading_chunk(1, 2)
        assert chunk == "What a"
        chunk2 = entry.reading_chunk(1, 2)
        assert chunk2 == "day of"

    def test_reading_entire_contents_in_chunks(self):
        entry = DiaryEntry("Day One", "What a day of test driving classes")
        chunk = entry.reading_chunk(1, 4)
        assert chunk == "What a day of"
        chunk2 = entry.reading_chunk(1, 100)
        assert chunk2 == "test driving classes"

    def test_reading_contents_again(self):
        entry = DiaryEntry("Day One", "What a day of test driving classes")
        chunk = entry.reading_chunk(1, 4)
        assert chunk == "What a day of"
        chunk2 = entry.reading_chunk(1, 1000000)
        assert chunk2 == "test driving classes"
        chunk3 = entry.reading_chunk(1, 5)
        assert chunk3 == "What a day of test"
