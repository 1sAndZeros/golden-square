from ..lib.Diary import Diary


class TestDiary:
    def test_instance_initialises_correctly(self):
        diary = Diary()
        assert diary.entries == []
