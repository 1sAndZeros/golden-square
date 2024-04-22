from lib.report_length import report_length


def test_check_hello_lowercase_returns_five_in_str_output():
    assert report_length("hello") == "This string was 5 characters long."


def test_check_hi_title_case_returns_two_in_str_output():
    assert report_length("Hi") == "This string was 2 characters long."


def test_check_goodbye_uppercase_returns_seven_in_str_output():
    assert report_length("GOODBYE") == "This string was 7 characters long."
