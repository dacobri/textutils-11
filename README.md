# textutils-11
# Group 11 - Python for Data Science Assignment 1

This project was created as part of the Python for Data course to practice Git collaboration, environment management, and collective software development workflows. Together, our team built and tested a small Python package called textutils, which performs a variety of text-processing functions.

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


# Implemented Features

unique_words(text)
Implemented by Caroline Wheeler
Extracts all distinct words from a given text, converts them to lowercase, and returns them in alphabetical order for easier analysis.

word_count(text)
Developed by Francesco Colpimeni
Calculates the total number of words in a string, serving as a foundational metric for text analytics.

is_anagram(text1, text2)
Created by Brice Da Costa and refined with input from Caroline Wheeler
Determines whether two strings are anagrams by comparing their character compositions after normalization.

capitalize_text(text)
Written by Francesco Colpimeni
Ensures that each word in the given text begins with a capital letter, improving readability and consistency.

tokenize(text)
Contributed collaboratively across the team
Cleans and standardizes input text by converting all characters to lowercase and removing punctuation, returning a structured list of alphanumeric tokens.

compare_texts(text1, text2)
Implemented by Simon Melk
Measures the textual similarity between two strings based on the ratio of shared unique words to all unique words.

is_palindrome(text)
Authored by Francesco Colpimeni
Checks whether a sentence reads the same forwards and backwards, ignoring case and spaces.

truncatestring(text, max_length)
Developed jointly by all team members
Shortens a text string to a defined maximum length and appends an ellipsis (...) when truncation occurs, ensuring the output remains readable.


# Team Members - GitHub Username
Caroline Wheeler - carolinesofiawheeler
Francesco Colpimeni - francescocolpimeni05-cmd
Brice Da Costa - dacobri
Simon - smelkk
