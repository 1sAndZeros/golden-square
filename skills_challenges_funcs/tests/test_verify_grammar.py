from ..lib.verify_grammar import *

# User story
"""As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter
and ends with a suitable sentence-ending punctuation mark."""

"""
Tests
no upper or punc
upper but no punc
no upper but punc
both upper and punc
check full stop
check exclamation mark
check question mark
"""


def test_false_when_no_uppercase_first_or_full_stop():
    assert verify_grammar("this is not correct") == False


def test_false_when_uppercase_but_no_puncuation():
    assert verify_grammar("This is not correct") == False


def test_false_when_no_uppercase_but_has_puncuation():
    assert verify_grammar("this is not correct.") == False


def test_correctly_formatted_sentence_with_full_stop():
    assert verify_grammar("This is a valid sentence.") == True


def test_correctly_formatted_sentence_with_exclamation():
    assert verify_grammar("This is also a valid sentence!") == True


def test_correctly_formatted_sentence_with_question_mark():
    assert verify_grammar("This is also a valid sentence?") == True
