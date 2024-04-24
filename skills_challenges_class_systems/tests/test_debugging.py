from ..lib.debugging import *


def test_factorial():
    assert factorial(5) == 120


def test_simple():
    remover = VowelRemover("ab")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "b"


def test_long_sentence_with_punctuation():
    remover = VowelRemover("We will remove the vowels from this sentence.")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "W wll rmv th vwls frm ths sntnc."


def test_all_vowels_returns_empty_string():
    remover = VowelRemover("aeiou")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == ""


def test_letter_counter():
    counter = LetterCounter("Digital Punk")
    assert counter.calculate_most_common() == [2, "i"]
    counter.text = "aaabcdeeEE"
    assert counter.calculate_most_common() == [4, "e"]
