from lib.check_codeword import check_codeword


def test_codeword_is_not_correct():
    assert check_codeword("donkey") == "WRONG!"


def test_codeword_is_correct():
    assert check_codeword("horse") == "Correct! Come in."


def test_codeword_is_close():
    assert check_codeword("headache") == "Close, but nope."
