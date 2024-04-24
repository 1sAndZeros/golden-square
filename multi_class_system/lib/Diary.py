class Diary:
    # User-facing properties:
    #   entries: list of DiaryEntry instances

    def __init__(self):
        self.entries = []

    def add(self, entry):
        # Parameters:
        #   entry: instance of a DiaryEntry
        # Returns: None
        # Side Effects:
        #   Adds a diary entry to the entries list
        self.entries.append(entry)

    def read_entry(self, title):
        # Parameters:
        #   title: string representing the title of the entry to read
        # Returns: string representing the contents of the entry
        for entry in self.entries:
            if entry.title == title:
                return entry.contents
        raise Exception("This diary entry doesn't exist")

    def read_entry_given_time(self, wpm, time_available):
        # Parameters:
        #   wpm: int representing the words the user can read per minute
        #   time_available: int representing minutes available to read
        # Returns: string representing the contents of the entry to read given the wpm and time given
        no_words_to_read = wpm * time_available
        entry_to_read = self.entries[0]
        for entry in self.entries:
            if no_words_to_read >= entry.count_words():
                if entry.count_words() > entry_to_read.count_words():
                    entry_to_read = entry
        if no_words_to_read < entry_to_read.count_words():
            return "There are no entries to read in the time given"
        else:
            return entry_to_read.contents

    def get_contacts(self):
        # Returns: list of strings representing all the contacts phone numbers in all stored diary entries
        numbers = [
            entry.get_phone_no()
            for entry in self.entries
            if entry.get_phone_no() != None
        ]
        return "No contacts exist" if len(numbers) == 0 else numbers
