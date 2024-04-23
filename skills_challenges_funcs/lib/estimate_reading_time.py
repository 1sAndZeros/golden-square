def estimate_reading_time(text):
    if text == "":
        raise Exception("Empty string not valid")
    words = text.split(" ")
    return round(200 / len(words), 2)
