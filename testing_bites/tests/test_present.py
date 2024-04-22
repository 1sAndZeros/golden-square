import pytest
from lib.present import Present


class TestPresent:
    def test_instance_initialises_correctly(self):
        present = Present()
        assert present.contents == None

    def test_wrap_method_updates_contents_when_none(self):
        present = Present()
        present.wrap("PS5")
        assert present.contents == "PS5"

    def test_wrap_method_raises_error_when_not_none(self):
        present = Present()
        present.wrap("PS5")
        with pytest.raises(Exception) as error:
            present.wrap("Laptop")
        assert str(error.value) == "A contents has already been wrapped."

    def test_unwrap_method_raises_error_when_none(self):
        present = Present()
        with pytest.raises(Exception) as error:
            present.unwrap()
        assert str(error.value) == "No contents have been wrapped."

    def test_unwrap_method_returns_contents(self):
        present = Present()
        present.wrap("PS5")
        assert present.unwrap() == "PS5"
