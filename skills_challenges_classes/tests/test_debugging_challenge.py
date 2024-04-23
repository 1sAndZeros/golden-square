from ..lib.debugging_challenge import get_most_common_letter


def test_most_common():
    assert get_most_common_letter("the roof, the roof, the roof is on fire!") == "o"
