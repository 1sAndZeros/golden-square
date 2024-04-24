# Tracker Multi-Class Planned Design Recipe

## 1. Describe the Problem

> As a user  
> So that I can record my experiences  
> I want to keep a regular diary
>
> As a user  
> So that I can reflect on my experiences  
> I want to read my past diary entries
>
> As a user  
> So that I can reflect on my experiences in my busy day  
> I want to select diary entries to read based on how much time I have and my
> reading speed
>
> As a user  
> So that I can keep track of my tasks  
> I want to keep a todo list along with my diary
>
> As a user  
> So that I can keep track of my contacts  
> I want to see a list of all of the mobile phone numbers in all my diary entries

## 2. Design the Class System

![Tracker Diagram](./diagram.jpeg)

```python
class Person:
    # User-facing properties:
    #   name: name of person

    def __init__(self, name):
        # Parameters:
        #   name: string representing persons name
        #   diary: instance of a Diary
        #   todo_list: instance of a TodoList
        pass # No code here yet

class Diary:
    # User-facing properties:
    #   entries: list of DiaryEntry instances

    def __init__(self):
        pass # No code here yet

    def add(self, entry):
        # Parameters:
        #   entry: instance of a DiaryEntry
        # Returns: None
        # Side Effects:
        #   Adds a diary entry to the entries list
        pass # No code here yet

    def read_entry(self, title):
        # Parameters:
        #   title: string representing the title of the entry to read
        # Returns: string representing the contents of the entry
        pass # No code here yet

    def read_entry_given_time(self, wpm, time_available):
        # Parameters:
        #   wpm: int representing the words the user can read per minute
        #   time_available: int representing minutes available to read
        # Returns: string representing the contents of the entry to read given the wpm and time given
        pass # No code here yet

    def get_contacts(self):
        # Returns: list of strings representing all the contacts phone numbers in all stored diary entries
        pass # No code here yet

class DiaryEntry:
    # User-facing properties:
    #   title: title of the entry
    #   contents: contents of the entry

    def __init__(self, title, contents):
        # Parameters:
        #   title: string representing title of the entry
        #   contents: string of the contents of the entry
        pass # No code here yet

    def count_words(self):
        # Returns: int representing number of words in the entry contents
        pass # No code here yet

    def get_phone_no(self):
        # Returns: string representing the contact number in the entry
        pass # No code here yet

class TodoList:
    # User-facing properties:
    #   todos: list of todo items

    def __init__(self):
        # Parameters:
        #   todos: list of todo instances
        pass # No code here yet

    def add(self, task):
        # Paramters:
        #   string representing description of the task
        pass # No code here yet

class Todo:
    # User-facing properties:
    #   task: name of the task
    #   complete: decribes whether the task is complete

    def __init__(self, task):
        # Parameters:
        #   task: string representing the name of the task
        #   complete: bool representing if task is complete
        pass # No code here yet

    def mark_complete(self):
        # Side effects:
        #   changes the complete property to True
        pass # No code here yet

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
"""
Create Diary and TodoList instances
Initialise a user with a name, Diary and TodoList
users name should be reflected
users diary should be reflected
users todo list shouild be reflected
"""
johns_diary = Diary()
johns_todo_list = TodoList()
john_smith = User('John Smith', diary=johns_diary, todo_list = johns_todo_list)
john_smith.name # => 'John Smith'
john_smith.diary # => johns_diary
john_smith.todo_list # => johns_todo_list

"""
Create instance of a diary and a diary entry
Add the diary entry to the diary
entry should be reflected in the diary
"""
my_diary = Diary()
entry1 = DiaryEntry('Entry One', 'This is my first diary entry')
my_diary.add(entry1)
my_diary.entries # => [entry1]

"""
Create instance of a diary and 2 diary entries
Add the diary entries to the diary
entries should be reflected in the diary
"""
my_diary = Diary()
entry1 = DiaryEntry('Entry One', 'This is my first diary entry')
my_diary.add(entry1)
entry2 = DiaryEntry('Entry Two', 'This is my second diary entry')
my_diary.add(entry2)
my_diary.entries # => [entry1, entry2]

"""
Create instance of a diary and 2 diary entries
Add the diary entries to the diary
read_entry with the diary title returns the contents
"""
my_diary = Diary()
entry1 = DiaryEntry('Entry One', 'This is my first diary entry')
my_diary.add(entry1)
entry2 = DiaryEntry('Entry Two', 'This is my second diary entry')
my_diary.add(entry2)
my_diary.read_entry('Entry Two') # => 'This is my second diary entry'

"""
Create instance of a diary and 2 diary entries
Add the diary entries to the diary
read_entry a diary title that doesn't exist returns Exception
"""
my_diary = Diary()
entry1 = DiaryEntry('Entry One', 'This is my first diary entry')
my_diary.add(entry1)
entry2 = DiaryEntry('Entry Two', 'This is my second diary entry')
my_diary.add(entry2)
my_diary.read_entry('Entry Three') # => Exception("This diary entry doesn't exist")

"""
Create instance of a diary and 2 diary entries
Add the diary entries to the diary
read_entry_given_time with wpm and time_available returns the contents of the longest entry the user can read
"""
my_diary = Diary()
entry1 = DiaryEntry('Entry One', 'This is my first diary entry')
my_diary.add(entry1)
entry2 = DiaryEntry('Entry Two', 'This is my second diary entry which is longer')
my_diary.add(entry2)
my_diary.read_entry_given_time(2,4) # => 'This is my first diary entry'
my_diary.read_entry_given_time(10,20) # => 'This is my second diary entry which is longer'

"""
Given a diary and 2 entries
when read_entry_given_time is called
if no entries are short enough to read
return message saying there are no entries to read in the time given
"""
my_diary = Diary()
entry1 = DiaryEntry('Entry One', 'This is my first diary entry')
my_diary.add(entry1)
entry2 = DiaryEntry('Entry Two', 'This is my second diary entry which is longer')
my_diary.add(entry2)
my_diary.read_entry_given_time(2,2) # => 'There are no entries to read in the time given'

"""
Given a diary and 2 entries including numbers
get_contacts returns a list of the numbers as strings
"""
my_diary = Diary()
entry1 = DiaryEntry('Entry One', 'This is my first diary entry. I called John on 12345678910')
my_diary.add(entry1)
entry2 = DiaryEntry('Entry Two', 'This is my second diary entry which is longer. I called Sarahs number which is 10987654321. We had a nice catch up')
my_diary.add(entry2)
my_diary.get_contacts() # => ['12345678910', '10987654321']

"""
Given a diary and 2 entries with no numbers
get_contacts returns a message saying "No contacts exist"
"""
my_diary = Diary()
entry1 = DiaryEntry('Entry One', 'This is my first diary entry')
my_diary.add(entry1)
entry2 = DiaryEntry('Entry Two', 'This is my second diary entry which is longer. I called Sarah and we had a nice catch up')
my_diary.add(entry2)
my_diary.get_contacts() # => 'No contacts exist'

"""
Given a todo list instance and multiple todos
when add is called with that todo
the todo is reflected in the todos list
along with the other todos added
"""
my_todo_list = TodoList()
task1 = Todo('Make a shopping list')
my_todo_list.add(task1)
my_todo_list.todos() # => [task1]
task2 = Todo('Buy the shopping')
my_todo_list.add(task2)
my_todo_list.todos # => [task1, task2]

```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python

"""
When a todoList is intialised
The todos list is empty
"""
my_list = TodoList()
my_list.todos # => []

"""
When a Todo is intialised with a task
the task name is reflected
complete should be false
"""
task1 = Todo('Go Shopping')
task1.task # => 'Go Shopping'
task1.complete # => False

"""
When a Todo is maked as complete
complete property should be True
"""
task1 = Todo('Go Shopping')
task1.mark_complete()
task1.complete # => True

"""
When a Diary entry is intialised with a title and contents
these are reflected in the entry
"""
entry1 = DiaryEntry('Entry One', 'This is a diary entry')
entry1.title # => 'Entry One'
entry1.contents # => 'This is a diary entry'

"""
When a Diary entry is intialised with a title and contents
and the count words method is called
It should return the number of words in the contents
"""
entry1 = DiaryEntry('Entry One', 'This is a diary entry')
entry1.count_words() # => 5

"""
When a Diary entry is intialised with a title and contents
and the count words method is called
It should return the number of words in the contents
"""
entry1 = DiaryEntry('Entry One', 'This is my first diary entry. I called John on 12345678910')
entry1.get_phone_no() # => '12345678910'

"""
When a Diary entry is intialised with a title and contents
and the count words method is called
It should return the number of words in the contents
"""
entry1 = DiaryEntry('Entry One', 'This is my first diary entry. I called John.')
entry1.get_phone_no() # => None

```