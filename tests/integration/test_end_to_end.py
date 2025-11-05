#Integration tests combining multiple core.py functions to validate full text-processing workflows.

import textutils.core as c

def test_unique_words_then_word_count():
    # Take unique words, then count how many there are
    text = "apple banana banana orange"
    unique = c.unique_words(text)  # ['apple', 'banana', 'orange']
    result = c.word_count(" ".join(unique))
    assert result == 3

def test_tokenize_then_compare_texts():
    # Tokenize two sentences and compare their similarity
    text1 = "Hello, world! This is AI."
    text2 = "hello world ai"
    tokens1 = c.tokenize(text1)
    tokens2 = c.tokenize(text2)
    similarity = c.compare_texts(" ".join(tokens1), " ".join(tokens2))
    assert similarity == 0.6

def test_capitalize_then_is_palindrome():
    # Capitalize a palindrome phrase and verify it still counts as palindrome
    text = "a man a plan a canal panama"
    capitalized = c.capitalize_text(text)
    assert c.is_palindrome(capitalized) is True

def test_truncate_then_add_exclamation():
    # Truncate a string and add an exclamation mark at the end
    text = "DataScienceRocks"
    truncated = c.truncatestring(text, 4)  # "Data"
    final = c.add_exclamation(truncated)  # "Data!"
    assert final == "Data!"

def test_to_lowercase_then_remove_spaces():
    # Make lowercase and remove spaces for normalization
    text = "  HeLLo   WoRLd  "
    lower = c.to_lowercase(text)
    cleaned = c.remove_spaces(lower)
    assert cleaned == "helloworld"

def test_remove_spaces_then_is_anagram():
    # Check if removing spaces allows detection of an anagram
    text1 = "Dormitory"
    text2 = "Dirty room"
    cleaned1 = c.remove_spaces(text1)
    cleaned2 = c.remove_spaces(text2)
    assert c.is_anagram(cleaned1, cleaned2) is True

def test_tokenize_then_count_vowels():
    # Tokenize text and count vowels in combined tokens
    text = "AI and Data Science!"
    tokens = c.tokenize(text)  # ['ai', 'and', 'data', 'science']
    joined = " ".join(tokens)
    vowel_count = c.count_vowels(joined)
    assert vowel_count == 8

def test_full_text_processing_pipeline():
    # Full multi-step test combining lowercase, remove spaces, and add exclamation
    text = "HeLLo WoRLD"
    normalized = c.to_lowercase(text)
    cleaned = c.remove_spaces(normalized)
    final = c.add_exclamation(cleaned)
    assert final == "helloworld!"

def test_text_pipeline_end_to_end():
    text = "HeLLo WoRLD "
    # Step 1: lowercase
    lower = c.to_lowercase(text)
    # Step 2: remove spaces
    no_spaces = c.remove_spaces(lower)
    # Step 3: add exclamation mark
    final = c.add_exclamation(no_spaces)

    # Final check
    assert final == "helloworld!"

