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