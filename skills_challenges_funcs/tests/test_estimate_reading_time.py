import pytest
from ..lib.estimate_reading_time import *

# User story
"""As a user
So that I can manage my time
I want to see an estimate of reading time for a text,
assuming that I can read 200 words a minute."""


def test_returns_1_given_200_words():
    # words = " ".join(["word" + i for i in range(200)]) # is it too complex for a test?
    words = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec quam nulla, vehicula quis euismod id, interdum vitae mi. Praesent turpis nibh, fermentum in fermentum tempus, lacinia a justo. Mauris imperdiet velit odio, non tristique nibh sollicitudin ac. Mauris et dolor eu purus imperdiet tincidunt quis et libero. Duis eleifend in tellus vel egestas. Cras lacinia mauris ac pellentesque aliquet. Suspendisse pharetra bibendum odio quis viverra. Praesent mauris massa, rutrum eu felis vel, ullamcorper scelerisque erat. Cras at ullamcorper diam, ac pulvinar orci. Aliquam quis tincidunt leo. Fusce enim ipsum, mattis et volutpat vitae, egestas sed metus. Aenean luctus odio neque, pellentesque interdum enim viverra eget. Sed non vehicula ligula. Donec euismod molestie dui, id cursus quam egestas cursus. Vivamus risus neque, pellentesque nec sodales a, vehicula id nulla. Phasellus purus quam, consectetur quis bibendum interdum, pharetra non dui. Proin ornare libero in dui finibus scelerisque. Fusce semper dictum erat, in convallis libero sodales eget. Quisque eleifend scelerisque dui, et hendrerit erat aliquet varius. Aenean venenatis, arcu a bibendum ullamcorper, metus ante aliquam erat, et commodo ante nisi eu magna. Pellentesque vel mollis sapien, sed maximus orci. Vestibulum gravida dapibus fermentum. Aliquam tempor tellus nec diam tristique elementum. Nullam in erat."
    assert estimate_reading_time(words) == 1


def test_returns_50_given_4_words():
    assert estimate_reading_time("This is a test") == 50


def test_returns_float_to_2dp_given_3_words():
    assert estimate_reading_time("three word test") == 66.67


def test_raises_error_when_empty_string():
    with pytest.raises(Exception, match="Empty string not valid"):
        estimate_reading_time("")
