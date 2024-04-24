class TrackRecorder:

    def __init__(self):
        self.tracks = []

    def add(self, track):
        # Parameters:
        #   track: string representing a single track
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the track to the self object
        self.tracks.append(track)

    def get_tracks(self):
        # Returns:
        #   list of all tracks
        return self.tracks
