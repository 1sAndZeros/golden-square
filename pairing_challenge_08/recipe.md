# BirthdayCards Class Design Recipe

## 1. Describe the Problem

<!-- self.friends = [
    {
        name: "John Smith",
        dob: "05/06/2000",
        card_sent: True
    }
] -->

<!-- found_friend = None
for friend in self.friends:
    if friend["name"] = "name given":
        found_friend = friend -->

As a user
So I don't forget the details
I want to keep a record of friends' names and birthdates

As a user
So I can make edits when I've got dates wrong
I want to be able to update a record by passing in a name and new date

As a user
So I can make edits when people change their name
I want to be able to update a record by passing in an old and a new name

As a user
So I can remember to send birthday cards at the right time
I want to be able to list friends whose birthdays are coming up soon and to whom I need to send a card

As a user
So I can buy age-appropriate birthday cards
I want to calculate the upcoming ages for friends with birthdays

As a user
So I can keep track of cards sent and to be sent
I want to be able to mark a birthday card for a year as "done"

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class BirthdayCards:
    # User-facing properties:
    #   friends: list[dict]

    def __init__(self):
        pass # No code here yet

    def add_friend(self, name, dob):
        # Parameters:
        #   name: string representing friends name
        #   dob: string representing date of birthday
        # Returns:
        #   Nothing
        # Side-effects
        #   Add friend dictionary to self.friends
        pass # No code here yet

    def update_friend(self, name, update, change):
        # Parameters:
        #   name: string representing friends name
        #   update: string representing new date of birth or new name
        #   change: string either dob or name
        # Returns:
        #   Nothing
        # Side-effects
        #   Updates friend with either new name or new dob
        pass

    def upcoming_birthdays_list(self, timeframe = 30):
        # Parameters:
        #   timeframe: int representing days to look ahead
        # Returns:
        #   list of friends who has a birthday within the timeframe
        pass

    def upcoming_ages(self):
        # Returns:
        #   list of tuples (name, age) who has a birthday coming up
        pass

    def mark_as_sent(self, name):
        # Parameters:
        #   name: string representing friends name
        # Side-effects
        #   Update card_sent to True for that name given

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

```python
# EXAMPLE

"""
Given a name and a task
#remind reminds the user to do the task
"""
reminder = Reminder("Kay")
reminder.remind_me_to("Walk the dog")
reminder.remind() # => "Walk the dog, Kay!"

"""
Given a name and no task
#remind raises an exception
"""
reminder = Reminder("Kay")
reminder.remind() # raises an error with the message "No task set."

"""
Given a name and an empty task
#remind still reminds the user to do the task, even though it looks odd
"""
reminder = Reminder("Kay")
reminder.remind_me_to("")
reminder.remind() # => ", Kay!"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
