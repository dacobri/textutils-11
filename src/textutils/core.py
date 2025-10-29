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

def is_anagram(text1, text2):
    #Checking for strings
    if type(text1) != str:
        raise TypeError("Input must be a string")
    if type(text2) != str:
        raise TypeError("Input must be a string")
    # Remove spaces and make lowercase
    text1 = text1.replace(" ", "").lower()
    text2 = text2.replace(" ", "").lower()
    
    # Sort the letters and compare
    return sorted(text1) == sorted(text2)

def capitalize_text(text):
    # Capitalize the first letter of each word in the text
    return text.title()