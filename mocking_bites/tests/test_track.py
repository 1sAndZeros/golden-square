from ..lib.Track import Track


class TestTrack:
    def test_track_initialises(self):
        track_one = Track("A Thing Called Love", "Above and Beyond")
        assert track_one.title == "A Thing Called Love"
        assert track_one.artist == "Above and Beyond"

    def test_true_when_title_matches(self):
        track_one = Track("A Thing Called Love", "Above and Beyond")
        assert track_one.matches("Love") == True

    def test_true_when_artist_matches(self):
        track_one = Track("A Thing Called Love", "Above and Beyond")
        assert track_one.matches("Above") == True

    def test_false_when_no_matches(self):
        track_one = Track("A Thing Called Love", "Above and Beyond")
        assert track_one.matches("Nothing") == False
