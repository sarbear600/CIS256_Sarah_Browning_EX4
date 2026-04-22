# Sarah Browning
# CIS256 Spring 2026
# Exercise Assignment 4

from guess_the_word import get_word, check_guess, guessing_words

# Test word comes from list
def test_word_in_list():
    word = get_word()
    assert word in guessing_words

# Test correct guess
def test_correct_guess():
    assert check_guess("pickle", "p") == True

# Test incorrect guess
def test_wrong_guess():
    assert check_guess("pickle", "r") == False
