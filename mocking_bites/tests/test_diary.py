from ..lib.Diary import Diary


class TestDiary:
    def test_diary_initialises(self):
        diary = Diary("This is the contents of my diary")
        assert diary.contents == "This is the contents of my diary"

    def test_read_method_returns_contents(self):
        diary = Diary("This is the contents of my diary")
        assert diary.read() == "This is the contents of my diary"
