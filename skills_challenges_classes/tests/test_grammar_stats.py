from ..lib.GrammarStats import GrammarStats


class TestGrammarStats:
    def test_instance_initialises_correctly(self):
        stats = GrammarStats()
        assert stats.num_good == 0
        assert stats.num_bad == 0

    def test_check_method(self):
        stats = GrammarStats()

        empty_string = ""
        assert stats.check(empty_string) == False

        with_upper_no_punctuation = "This is a test"
        assert stats.check(with_upper_no_punctuation) == False

        with_upper_and_punctuation = "This is a test."
        assert stats.check(with_upper_and_punctuation) == True

        with_no_upper_no_punctuation = "this is a test"
        assert stats.check(with_no_upper_no_punctuation) == False

        with_no_upper_but_has_punctuation = "this is a test."
        assert stats.check(with_no_upper_but_has_punctuation) == False

        with_upper_and_exclamation = "This is a test!"
        assert stats.check(with_upper_and_exclamation) == True

        with_upper_and_question_mark = "This is a test?"
        assert stats.check(with_upper_and_question_mark) == True

    def test_percentage_good(self):
        stats = GrammarStats()
        bad = "this is not correct"
        good = "This is formatted correctly!"

        stats.check(bad)
        assert stats.percentage_good() == 0

        stats.check(good)
        assert stats.percentage_good() == 50

        stats.check(good)
        assert stats.percentage_good() == 67

        stats.check(bad)
        assert stats.percentage_good() == 50

        stats.check(bad)
        assert stats.percentage_good() == 40
