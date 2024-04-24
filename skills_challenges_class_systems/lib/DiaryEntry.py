class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents):
        # Side-effects:
        #   Sets the title and contents properties

        self.title = title.strip()
        self.contents = contents.strip()
        self.words_read = 0

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry

        return len(self.contents.split(" "))

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.

        return int(self.count_words() / wpm)

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.

        no_of_words_we_can_read = wpm * minutes
        chunk = self.contents.split()[
            self.words_read : self.words_read + no_of_words_we_can_read
        ]
        self.words_read += no_of_words_we_can_read
        if self.words_read > self.count_words():
            self.words_read = 0
        return " ".join(chunk)
