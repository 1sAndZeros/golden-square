# {{PROBLEM}} Class Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class TrackRecorder:

    def __init__(self):
        pass # No code here yet

    def add(self, track):
        # Parameters:
        #   track: string representing a single track
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the track to the self object
        pass # No code here yet

    def get_tracks(self):
        # Returns:
        #   list of all tracks
        pass

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

```python

"""
Test track list is empty on initialisation
"""
track_recorder = TrackRecorder()
track_recorder.get_tracks() # => []

"""
Adds a single entry to track list
"""
track_recorder = TrackRecorder()
track_recorder.add("Wonderwall")
track_recorder.get_tracks() # => ["Wonderwall"]

"""
Adds multiple entries to track list
"""
track_recorder = TrackRecorder()
track_recorder.add("Wonderwall")
track_recorder.add("What's The Story Morning Glory")
track_recorder.get_tracks() # => ["Wonderwall", "What's The Story Morning Glory"]

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
