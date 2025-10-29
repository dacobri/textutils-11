import textutils.core as c

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
    assert c.compare_texts("", "something") == 0.0