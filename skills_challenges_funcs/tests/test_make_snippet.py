from ..lib.make_snippet import make_snippet

def test_function_returns_all_words_when_given_five_words():
    assert make_snippet("This is my first test") == "This is my first test"
