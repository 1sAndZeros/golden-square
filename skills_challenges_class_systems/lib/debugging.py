def factorial(n):
    product = 1
    while n > 1:
        product *= n
        n -= 1
    return product


class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        i = 0
        while i < len(self.text):
            if self.text[i].lower() in self.vowels:
                self.text = self.text[:i] + self.text[i + 1 :]
                i -= 1
            i += 1
        return self.text


class LetterCounter:
    def __init__(self, text):
        self.text = text

    def calculate_most_common(self):
        counter = {}
        most_common = None
        most_common_count = 1
        for char in self.text:
            if not char.isalpha():
                continue
            char = char.lower()
            counter[char] = counter.get(char, 0) + 1
            if counter[char] > most_common_count:
                most_common = char
                most_common_count = counter[char]
        return [most_common_count, most_common]
