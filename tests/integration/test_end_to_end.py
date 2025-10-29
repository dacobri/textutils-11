import textutils.core as c

def test_unique_words_after_normalization():
    # Uses two functions together: normalize_whitespace & unique_words
    text = "Red   red    BLUE"
    normalized = c.normalize_whitespace(text)   # should become "Red red BLUE"
    result = c.unique_words(normalized)         # lowercases + uniques + sorts
    assert result == ["blue", "red"]

def test_unique_words_consistent_with_word_count_keys():
    # word_count and unique_words should agree on the distinct tokens
    text = "Dog dog CAT"
    counts = c.word_count(text)                 # e.g., {"dog": 2, "cat": 1}
    uniques = c.unique_words(text)              # ["cat", "dog"]
    assert sorted(counts.keys()) == uniques