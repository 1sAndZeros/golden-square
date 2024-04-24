import re


class DiaryEntry:
    # User-facing properties:
    #   title: title of the entry
    #   contents: contents of the entry

    def __init__(self, title, contents):
        # Parameters:
        #   title: string representing title of the entry
        #   contents: string of the contents of the entry
        self.title = title
        self.contents = contents

    def count_words(self):
        # Returns: int representing number of words in the entry contents
        words = self.contents.split()
        return len(words)

    def get_phone_no(self):
        # Returns: string representing the contact number in the entry
        regex = r"\d{11}"
        match = re.search(regex, self.contents)
        if match:
            return match.group(0)
