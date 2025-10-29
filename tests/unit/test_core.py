import textutils.core as c

def test_unique_words_sorted_and_lowercase():
    result = c.unique_words("Dog dog Cat")
    assert result == ["cat", "dog"]
    
def test_unique_words_trims_spaces():
    result = c.unique_words("  hi   hi ")
    assert result == ["hi"]