#Unit tests for individual functions in core.py to ensure correctness and handle edge cases.

import textutils.core as c

def test_unique_words_sorted_and_lowercase(): 
    result = c.unique_words("Dog dog Cat") 
    assert result == ["cat", "dog"] 
    
def test_unique_words_trims_spaces(): 
    result = c.unique_words(" hi hi ") 
    assert result == ["hi"]

def test_unique_words_invalid_type():
    try:
        c.unique_words(123)
        assert False, "Expected TypeError for non-string input"
    except TypeError:
        assert True

def test_is_anagram_invalid_first_argument():
    try:
        c.is_anagram(123, "abc")
        assert False, "Expected TypeError for first argument"
    except TypeError:
        assert True

def test_is_anagram_invalid_second_argument():
    try:
        c.is_anagram("abc", 456)
        assert False, "Expected TypeError for second argument"
    except TypeError:
        assert True

def test_truncatestring_negative_length():
    # Negative max_length should return an empty string
    assert c.truncatestring("hello", -5) == ""

def test_capitalize_text():
    # Capitalizes each word correctly
    assert c.capitalize_text("hello world") == "Hello World"
    # Empty string remains unchanged
    assert c.capitalize_text("") == ""
    # Multiple words capitalize properly
    assert c.capitalize_text("python for data science") == "Python For Data Science"

def test_compare_texts_identical():
    t = "a b c"
    assert c.compare_texts(t, t) == 1.0

def test_compare_texts_partial_overlap():
    t1 = "apple banana"
    t2 = "banana cherry"
    assert c.compare_texts(t1, t2) == 1/3

def test_compare_texts_empty_cases():
    assert c.compare_texts("", "") == 1.0
    assert c.compare_texts("", "something") == 0.
    

def test_is_palindrome_true():
    assert c.is_palindrome("Race car") is True
    assert c.is_palindrome("madam") is True
    assert c.is_palindrome("A man a plan a canal Panama") is True

def test_is_palindrome_false():
    assert c.is_palindrome("hello") is False
    assert c.is_palindrome("Python") is False

def test_is_palindrome_empty_or_single_char():
    assert c.is_palindrome("") is True     # empty string counts as palindrome
    assert c.is_palindrome("a") is True  

def test_word_count():
    # Test 1: Simple sentence
    assert c.word_count("Hello world") == 2

    # Test 2: Sentence with punctuation
    assert c.word_count("Artificial intelligence, machine learning, and data science!") == 7

    # Test 3: Sentence with multiple spaces
    assert c.word_count("  This   has   extra   spaces  ") == 4

    # Test 4: Empty string
    assert c.word_count("") == 0

    print("All tests passed!")



def test_truncatestring_short_text():
    # Text shorter than max_length → unchanged
    assert c.truncatestring("hello", 10) == "hello"

def test_truncatestring_exact_length():
    # Text exactly equal to max_length → unchanged
    assert c.truncatestring("hello", 5) == "hello"

def test_truncatestring_long_text():
    # Text longer than max_length → truncated
    assert c.truncatestring("hello world", 5) == "hello"

def test_truncatestring_empty_text():
    # Empty text should remain empty
    assert c.truncatestring("", 5) == ""

def test_truncatestring_zero_length():
    # max_length = 0 should return an empty string
    assert c.truncatestring("abcdef", 0) == ""

def test_word_count_basic():
    text = "This is a simple test"
    assert c.word_count(text) == 5

def test_count_vowels():
    # Test with mixed case and punctuation
    assert c.count_vowels("Hello, World!") == 3  # e, o, o
    # Test with no vowels
    assert c.count_vowels("rhythm") == 0
    # Test with all vowels
    assert c.count_vowels("AEIOUaeiou") == 10
    # Test with empty string
    assert c.count_vowels("") == 0

def test_to_lowercase():
    # Test with mixed case
    assert c.to_lowercase("HeLLo WoRLD") == "hello world"
    # Test with all uppercase
    assert c.to_lowercase("PYTHON") == "python"
    # Test with all lowercase (should stay the same)
    assert c.to_lowercase("already lowercase") == "already lowercase"
    # Test with empty string
    assert c.to_lowercase("") == ""

def test_remove_spaces():
    # Test with regular spaces
    assert c.remove_spaces("hello world") == "helloworld"
    # Test with multiple spaces
    assert c.remove_spaces("a  b   c") == "abc"
    # Test with no spaces
    assert c.remove_spaces("nospace") == "nospace"
    # Test with empty string
    assert c.remove_spaces("") == ""

def test_add_exclamation():
    # Test with a normal word
    assert c.add_exclamation("hello") == "hello!"
    # Test with sentence
    assert c.add_exclamation("this is fun") == "this is fun!"
    # Test when it already ends with "!"
    assert c.add_exclamation("wow!") == "wow!!"
    # Test with empty string
    assert c.add_exclamation("") == "!"