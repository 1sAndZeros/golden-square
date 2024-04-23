from ..lib.make_snippet import make_snippet


def test_retruns_all_words_given_less_than_five_words():
    assert make_snippet("My First Test") == "My First Test"


def test_function_returns_all_words_when_given_five_words():
    assert make_snippet("This is my second test") == "This is my second test"


def test_function_truncates_more_than_five_words():
    assert make_snippet("This is my third and final test") == "This is my third and..."


def test_function_truncates_more_than_five_words():
    assert (
        make_snippet(
            "Actually, I need another test. This one has punction marks! Don't forget about edge cases!!!"
        )
        == "Actually, I need another test...."
    )
