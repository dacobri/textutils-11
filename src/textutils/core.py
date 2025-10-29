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

def tokenize(text: str):
    #Split text into lowercase words (letters/numbers only)
    if not text:
        return []
    cleaned = ""
    for ch in text.lower():
        if ch.isalnum() or ch.isspace():
            cleaned += ch
        else:
            cleaned += " " 
    return cleaned.split()

def compare_texts(text1: str, text2: str) -> float:
    #Compute similarity = |common words| / |all unique words|.
    #Return 1.0 if both texts are empty.
    set1 = set(tokenize(text1))
    set2 = set(tokenize(text2))
    union = set1 | set2
    if not union:
        return 1.0
    return len(set1 & set2) / len(union)