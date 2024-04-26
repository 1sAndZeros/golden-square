from ..lib.SecretDiary import SecretDiary
from ..lib.Diary import Diary
import pytest


class TestDiaryIntegration:
    def test_secret_diary_initialises(self):
        diary = Diary("These are the contents of my diary")
        secret_diary = SecretDiary(diary)
        assert secret_diary.diary == diary
        assert secret_diary.locked == True

    def test_read_method_raises_error_when_locked(self):
        diary = Diary("These are the contents of my diary")
        secret_diary = SecretDiary(diary)
        with pytest.raises(Exception, match="Go away!"):
            secret_diary.read()

    def test_unlock_method_sets_locked_false(self):
        diary = Diary("These are the contents of my diary")
        secret_diary = SecretDiary(diary)
        assert secret_diary.locked == True
        secret_diary.unlock()
        assert secret_diary.locked == False

    def test_lock_method_locks_diary(self):
        diary = Diary("These are the contents of my diary")
        secret_diary = SecretDiary(diary)
        assert secret_diary.locked == True
        secret_diary.unlock()
        assert secret_diary.locked == False
        secret_diary.lock()
        assert secret_diary.locked == True

    def test_read_method_when_unlocked(self):
        diary = Diary("These are the contents of my diary")
        secret_diary = SecretDiary(diary)
        secret_diary.unlock()
        assert secret_diary.read() == "These are the contents of my diary"
