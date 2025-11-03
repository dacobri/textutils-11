import textutils.core as c
from textutils.core import is_palindrome

def test_unique_words_sorted_and_lowercase(): 
    result = c.unique_words("Dog dog Cat") 
    assert result == ["cat", "dog"] 
    
def test_unique_words_trims_spaces(): 
    result = c.unique_words(" hi hi ") 
    assert result == ["hi"]

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