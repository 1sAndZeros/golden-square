from ..lib.TrackerRecorder import TrackRecorder


def test_track_list_empty():
    """
    Test track list is empty on initialisation
    """

    track_recorder = TrackRecorder()
    assert track_recorder.get_tracks() == []


def test_add_a_single_track():
    """
    Adds a single entry to track list
    """
    track_recorder = TrackRecorder()
    track_recorder.add("Wonderwall")
    assert track_recorder.get_tracks() == ["Wonderwall"]


def test_add_multiple_tracks():
    """
    Adds multiple entries to track list
    """
    track_recorder = TrackRecorder()
    track_recorder.add("Wonderwall")
    track_recorder.add("What's The Story Morning Glory")
    assert track_recorder.get_tracks() == [
        "Wonderwall",
        "What's The Story Morning Glory",
    ]
