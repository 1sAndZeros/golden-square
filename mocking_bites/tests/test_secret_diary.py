from ..lib.SecretDiary import SecretDiary
from unittest.mock import Mock
import pytest


class TestSecretDiary:
    def test_secret_diary_initialises(self):
        mock_diary = Mock()
        secret_diary = SecretDiary(mock_diary)
        assert secret_diary.diary == mock_diary
        assert secret_diary.locked == True

    def test_read_method_raises_error_when_locked(self):
        mock_diary = Mock()
        secret_diary = SecretDiary(mock_diary)
        with pytest.raises(Exception, match="Go away!"):
            secret_diary.read()

    def test_unlock_method_sets_locked_false(self):
        mock_diary = Mock()
        secret_diary = SecretDiary(mock_diary)
        assert secret_diary.locked == True
        secret_diary.unlock()
        assert secret_diary.locked == False

    def test_lock_method_locks_diary(self):
        mock_diary = Mock()
        secret_diary = SecretDiary(mock_diary)
        assert secret_diary.locked == True
        secret_diary.unlock()
        assert secret_diary.locked == False
        secret_diary.lock()
        assert secret_diary.locked == True

    def test_read_method_when_unlocked(self):
        mock_diary = Mock()
        mock_diary.contents = "This is my diary"
        secret_diary = SecretDiary(mock_diary)
        secret_diary.unlock()
        assert secret_diary.read() == "This is my diary"
