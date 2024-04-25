from ..lib.MusicLibrary import MusicLibrary
from ..lib.Track import Track


class TestMusicIntegration:

    def test_single_track_is_added(self):
        library = MusicLibrary()
        track_one = Track("A Thing Called Love", "Above and Beyond")
        library.add(track_one)
        assert library.tracks == [track_one]

    def test_multiple_tracks_are_added(self):
        library = MusicLibrary()
        track_one = Track("A Thing Called Love", "Above and Beyond")
        track_two = Track("End Credits", "Chase and Status")
        library.add(track_one)
        library.add(track_two)
        assert library.tracks == [track_one, track_two]

    def test_search_finds_matching_tracks(self):
        library = MusicLibrary()
        track_one = Track("A Thing Called Love", "Above and Beyond")
        track_two = Track("End Credits", "Chase and Status")
        library.add(track_one)
        library.add(track_two)
        assert library.search("End") == [track_two]
        assert library.search("Status") == [track_two]
        assert library.search("Called") == [track_one]
        assert library.search("Beyond") == [track_one]
        assert library.search("and") == [track_one, track_two]
