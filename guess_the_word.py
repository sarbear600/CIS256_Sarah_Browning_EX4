# Sarah Browning 
# CIS 256 Spring 2026
# Exercise Assignment 4

import random

# List of different words for the word game
guesing_words = ["pickle", "rock", "dog", "tractor", "bark", "lamp" ]

def get_word():
    return random.choice(guesing_words)

#
def game(word, guessed_letter)
    display = "_"
    for letter in word:
        if letter in guessed_letter:
            display = letter

    return display
def check_guess(word, guess)
    return guess in word

def play_game():
    word = get_word()
    guessed_letter = []

    print("It's game time!")

    while turns > 0:
        print("This is how you play. You are going to guess letters to figure out what the word is.")
        guess = input("Guess a letter:")
        guessed_letter.append(guess)
        if check_guess(word, guess):
            print("correct")
        else:
            print("wrong")
            attempts -= 1

        if game(word, guessed_letter) == word:
            print("Good job, you guessed the word!")

    print("Sorry you didn't get it. The word was: ", word  "Play again to guess another word")

play_game()
