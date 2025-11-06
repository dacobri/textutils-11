# Group 11 — Python for Data Science Assignment 1

This repository was created as part of the Python for Data Science course to practice Git collaboration, environment management, and test-driven development (TDD).
Our team built a small Python package — textutils — that performs various text-processing operations with both unit and integration tests to ensure functionality and maintainability.

# Environment Setup
To recreate the development environment used for this project:
1.	Clone the repository:
"git clone https://github.com/dacobri/textutils-11.git"
"cd textutils-11/textutils"

2.	Create the environment using the provided environment.yml file:
"micromamba create -n textutils -f environment.yml"
"micromamba activate textutil"


# Installation
Once the environment is active, install the package in editable mode:
"pip install -e ."

This allows you to make changes to the source code and test them immediately without reinstalling.


# Running Tests
To verify that all functions work as intended, run:
"pytest"

For a coverage report:
"pytest --cov"

For specific tests (for example, only integration):
pytest -k full_text_pipeline

# Implemented Features
unique_words(text)
Implemented by Caroline Wheeler
Returns a sorted list of distinct, lowercase words found in the text.

word_count(text)
Developed by Francesco Polimeni
Returns the total number of words in the string (whitespace-separated), handling extra spaces cleanly.

is_anagram(text1, text2)
Created by Brice Da Costa and refined with input from Caroline Wheeler
Checks whether two texts are anagrams ignoring spaces and case.

capitalize_text(text)
Written by Francesco Polimeni
Returns the text with each word capitalized (title-style).

tokenize(text)
Contributed collaboratively across the team
Converts to lowercase, removes punctuation, and returns a list of alphanumeric tokens.

compare_texts(text1, text2)
Implemented by Simon
Computes similarity as |common unique words| ÷ |all unique words| (Jaccard ratio).

is_palindrome(text)
Authored by Francesco Polimeni
Returns True if the text reads the same forward and backward, ignoring spaces and case.

truncatestring(text, max_length)
Developed jointly by all team members
Returns the text truncated to max_length characters (no ellipsis added). If shorter, returns unchanged.

count_vowels(text)
Written by Francesco Polimeni
Counts the number of vowels (a, e, i, o, u) in the text, case-insensitive.


# Testing Overview
Unit tests (in tests/unit/test_core.py) verify each function individually.

Integration test (in tests/integration/test_end_to_end.py) checks that all functions work together within a complete text-processing workflow.

The Jupyter Notebook (A1.ipynb) documents the development and testing process step by step.


# Project Highlights
- Applied TDD (Test-Driven Development) and Git branching workflow.
- Demonstrated team collaboration via individual feature branches and merges.
- Built a reproducible Python environment using micromamba and pyproject.toml configuration.
- Ensured software reliability through pytest unit and integration tests.


# Team Members - GitHub Username
Caroline Wheeler - carolinesofiawheeler
Francesco Polimeni - francescopolimeni05-cmd
Brice Da Costa - dacobri
Simon - smelkk