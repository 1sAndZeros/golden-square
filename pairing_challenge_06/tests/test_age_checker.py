from ..lib.age_checker import *
import pytest


def test_user_is_over_16():
    actual = age_checker("1990-09-06")
    expected = "Access granted"
    assert actual == expected


def test_user_is_under_16():
    actual = age_checker("2020-09-06")
    expected = "Access denied"
    assert actual == expected


def test_user_is_16():
    actual = age_checker("2008-01-25")
    expected = "Access granted"
    assert actual == expected


def test_date_is_incorrect_format():
    with pytest.raises(Exception) as e:
        age_checker("2008/06/25")
    assert str(e.value) == "Incorrect format (yyyy-mm-dd)"
