# Sarah Browning 
# CIS 256 Spring 2026
# Exercise Assignment 4

import random

# List of different words for the word game
guesing_words = ["pickle", "rock", "dog", "tractor", "bark"]

def get_word():
    return random.choice(guesing_words)

def game(word, guess_letter):
    display = ""
    for letter in word:
        if letter in guess_letter:
            display += letter + " "
        else:
            display += "_"
    return display.strip()

def check_guess(word, guess):
    return guess in word

def play_game():
    word = get_word()
    guessed_letter = []
    turns = 8

    print("It's game time!")
    print("This is how you play. You are going to guess letters to figure out what the word is.")

    while turns > 0:
        print("word:", game(word, guessed_letter))
        print("You have this many trys: ", turns)

        guess = input("Guess a letter:").lower()
        
        if guess in guessed_letter:
            print("You already guessed that letter, try again.")
            continue

        guessed_letter.append(guess)

        if check_guess(word, guess):
            print("correct")
        else:
            print("wrong")
            turns -= 1

        if "_" not in game(word, guessed_letter):
            print("Good job, you guessed the word!")
            return

    print("Sorry you didn't get it. The word was: ", word,  "Play again to guess another word")

while True:
    play_game()

    repeat_game = input("Do you want to play again yes(Y) or no(N): ").lower()
    if repeat_game == "y":
        print("Lets play again")
        continue
    else: 
        print("Thanks for playing")
        break
