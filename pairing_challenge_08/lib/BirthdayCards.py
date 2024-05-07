from datetime import datetime
from dateutil.relativedelta import *


class BirthdayCards:
    # User-facing properties:
    #   friends: list[dict]

    def __init__(self):
        self.friends = []

    def add_friend(self, name, dob):
        # Parameters:
        #   name: string representing friends name
        #   dob: string representing date of birthday
        # Returns:
        #   Nothing
        # Side-effects
        #   Add friend dictionary to self.friends
        friend = {"name": name, "dob": dob, "card_sent": False}
        self.friends.append(friend)

    def update_friend(self, name, update, change):
        # Parameters:
        #   name: string representing friends name
        #   update: string representing new date of birth or new name
        #   change: string either dob or name
        # Returns:
        #   Nothing
        # Side-effects
        #   Updates friend with either new name or new dob
        for friend in self.friends:
            if friend["name"] == name:
                friend[change] = update
                break

    def upcoming_birthdays_list(self, timeframe=30):
        # Parameters:
        #   timeframe: int representing days to look ahead
        # Returns:
        #   list of friends who has a birthday within the timeframe
        res = []
        for friend in self.friends:
            date = datetime.strptime(friend["dob"], "%d/%m/%Y")
            now = datetime.now()
            date = date.replace(year=2024)
            diff = (date - now).days
            if 0 < diff < timeframe:
                res.append(friend)
        return res

    def upcoming_ages(self):
        # Returns:
        #   list of tuples (name, age) who has a birthday coming up
        people = self.upcoming_birthdays_list()
        res = []
        for friend in people:
            date = datetime.strptime(friend["dob"], "%d/%m/%Y")
            now = datetime.now()
            upcoming_age = relativedelta(now, date).years + 1
            res.append((friend["name"], upcoming_age))
        return res

    def mark_as_sent(self, name):
        # Parameters:
        #   name: string representing friends name
        # Side-effects
        #   Update card_sent to True for that name given
        for friend in self.friends:
            if friend["name"] == name:
                friend["card_sent"] = True
                break
