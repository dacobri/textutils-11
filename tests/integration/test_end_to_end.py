import textutils.core as c

# Integration: normalize_whitespace in unique_words
def test_unique_words_simple_pipeline():
    text = "  Dog   dog \n  Cat  "
    normalized = c.normalize_whitespace(text)  
    uniques = c.unique_words(normalized)       
    assert uniques == ["cat", "dog"]