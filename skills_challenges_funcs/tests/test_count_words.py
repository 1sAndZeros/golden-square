import pytest
from ..lib.count_words import count_words


def test_returns_5_given_five_words():
    assert count_words("This is my first test") == 5


def test_returns_num_of_words_given_a_paragraph():
    assert (
        count_words(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas auctor leo purus, in scelerisque nunc molestie in. Suspendisse nec augue."
        )
        == 20
    )


def test_errors_when_given_empty_string():
    with pytest.raises(Exception) as e:
        count_words("")
    assert str(e.value) == "Empty string cannot be given"
