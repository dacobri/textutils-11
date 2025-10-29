#Checking for unique words in a text
def unique_words(text):
    if type(text) != str:
        raise TypeError("Input must be a string")

    words = text.lower().split()
    unique = set(words)
    return sorted(unique)

def word_count(text):
    # Count the number of words in the given text
    words = text.split()
    return len(words)
def capitalize_text(text):
    # Capitalize the first letter of each word in the text
    return text.title()