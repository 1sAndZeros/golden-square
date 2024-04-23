def make_snippet(string):
    words = string.split(" ")
    return string if len(words) <= 5 else " ".join(words[:5]) + "..."
