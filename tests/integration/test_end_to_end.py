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

    # Extra: additional tests for word_count
    assert c.word_count("") == 0
    assert c.word_count("   spaced   words   ") == 2
    assert c.word_count("One two three four five") == 5

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


    # 6) is_palindrome: works after cleaning spaces and casing
    assert c.is_palindrome("Race car") is True
    assert c.is_palindrome("Python") is False
    assert c.is_palindrome("") is True

    # 7) truncatestring: trims to max length, keeps shorter/empty as-is
    assert c.truncatestring("hello world", 5) == "hello"
    assert c.truncatestring("hello", 5) == "hello"
    assert c.truncatestring("", 3) == ""
    assert c.truncatestring("abcdef", 0) == ""