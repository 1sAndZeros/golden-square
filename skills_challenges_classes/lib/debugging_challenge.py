def get_most_common_letter(text):
    text = text.replace(" ", "")
    counter = {}
    for char in text:
        counter[char] = counter.get(char, 0) + 1
    letter = sorted(counter.items(), key=lambda item: item[1])[-1][0]
    return letter
