# File: lib/high_value.py

class HighValue:
    def __init__(self, value_first, value_second):
        self.value_first = value_first
        self.value_second = value_second
    def get_highest(self):
        if self.value_first > self.value_second:
            return "First value is higher"
        elif self.value_first < self.value_second:
            return "Second value is higher"
        else:
            return "Values are equal"
    def add(self, increase_by, selection):
        if selection == "first":
            self.value_first += increase_by
        elif selection == "second":
            self.value_second += increase_by
