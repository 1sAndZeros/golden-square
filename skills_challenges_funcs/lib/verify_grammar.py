def verify_grammar(text):
    return text[0] == text[0].upper() and text[-1] in ".!?"
