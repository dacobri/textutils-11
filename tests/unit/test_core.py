import textutils.core as c
from textutils.core import is_palindrome
from textutils.core import word_count
from textutils.core import truncatestring

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
    assert is_palindrome("Race car") is True
    assert is_palindrome("madam") is True
    assert is_palindrome("A man a plan a canal Panama") is True

def test_is_palindrome_false():
    assert is_palindrome("hello") is False
    assert is_palindrome("Python") is False

def test_is_palindrome_empty_or_single_char():
    assert is_palindrome("") is True     # empty string counts as palindrome
    assert is_palindrome("a") is True  

def test_word_count():
    # Test 1: Simple sentence
    assert word_count("Hello world") == 2

    # Test 2: Sentence with punctuation
    assert word_count("Artificial intelligence, machine learning, and data science!") == 7

    # Test 3: Sentence with multiple spaces
    assert word_count("  This   has   extra   spaces  ") == 4

    # Test 4: Empty string
    assert word_count("") == 0

    print("All tests passed!")


def test_truncatestring_short_text():
    # Text shorter than max_length → unchanged
    assert truncatestring("hello", 10) == "hello"

def test_truncatestring_exact_length():
    # Text exactly equal to max_length → unchanged
    assert truncatestring("hello", 5) == "hello"

def test_truncatestring_long_text():
    # Text longer than max_length → truncated
    assert truncatestring("hello world", 5) == "hello"

def test_truncatestring_empty_text():
    # Empty text should remain empty
    assert truncatestring("", 5) == ""

def test_truncatestring_zero_length():
    # max_length = 0 should return an empty string
    assert truncatestring("abcdef", 0) == ""