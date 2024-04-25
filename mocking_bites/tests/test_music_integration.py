from ..lib.MusicLibrary import MusicLibrary
from unittest.mock import Mock


class TestMusicLibrary:
    def test_library_initialises(self):
        library = MusicLibrary()
        assert library.tracks == []

    def test_single_track_is_added(self):
        library = MusicLibrary()
        track_one = Mock()
        library.add(track_one)
        assert library.tracks == [track_one]

    def test_multiple_tracks_are_added(self):
        library = MusicLibrary()
        track_one = Mock()
        track_two = Mock()
        library.add(track_one)
        library.add(track_two)
        assert library.tracks == [track_one, track_two]

    def test_search_finds_matching_track(self):
        library = MusicLibrary()
        track_one = Mock()
        track_two = Mock()
        library.add(track_one)
        library.add(track_two)
        track_one.matches.return_value = False
        track_two.matches.return_value = True
        assert library.search("keyword") == [track_two]
