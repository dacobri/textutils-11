#Checking for unique words in a text
def unique_words(text):
    if type(text) != str:
        raise TypeError("Input must be a string")

    words = text.lower().split()
    unique = set(words)
    return sorted(unique)