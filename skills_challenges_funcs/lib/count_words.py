def count_words(string):
    if string == "":
        raise Exception("Empty string cannot be given")
    return len(string.split(" "))
