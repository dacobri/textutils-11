import textutils.core as c

def test_full_text_pipeline():
    # Inputs
    text1 = "apple banana banana"
    text2 = "banana cherry apple"

    # 1) unique_words: lowercase + unique + sorted
    uniq1 = c.unique_words(text1)
    assert uniq1 == ["apple", "banana"]

    # 2) word_count: simple whitespace split count
    count2 = c.word_count(text2)
    assert count2 == 3

    # 3) tokenize: punctuation removed, lowercase words kept
    assert c.tokenize("Hello, world!! 42") == ["hello", "world", "42"]

    # 4) is_anagram: ignore case and spaces
    assert c.is_anagram("Listen", "Silent") is True
    assert c.is_anagram("Dormitory", "Dirty room") is True
    assert c.is_anagram("Apple", "Plead") is False

    # 5) compare_texts: Jaccard-like similarity of word sets
    # set(text1) = {apple, banana}, set(text2) = {banana, cherry, apple}
    # intersection = 2, union = 3 -> 2/3
    sim = c.compare_texts(text1, text2)
    assert sim == 2/3