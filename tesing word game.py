# Sarah Browning
# CIS256 Spring 2026
# Exercise Assignment 4

import random

# word list
word_list = ["apple", "banana", "grape", "orange"]

# pick random word
def get_word():
    return random.choice(word_list)

# display current progress
def get_display(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

# check guess
def check_guess(word, guess):
    return guess in word


def play_game():
    word = get_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman-style Guess the Word!")

    while attempts > 0:
        print("\nWord:", get_display(word, guessed_letters))
        print("Attempts left:", attempts)

        guess = input("Guess a letter: ").lower()

        # prevent duplicate guesses
        if guess in guessed_letters:
            print("You already guessed that!")
            continue

        guessed_letters.append(guess)

        if check_guess(word, guess):
            print("Correct!")
        else:
            print("Wrong!")
            attempts -= 1

        # check win
        if "_" not in get_display(word, guessed_letters):
            print("\nCongrats! You guessed the word:", word)
            return

    print("\nGame over. The word was:", word)


play_game()