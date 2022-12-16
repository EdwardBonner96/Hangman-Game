# Allows random number generation
import random

# ASCII art for lives, from https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words_list = ['testone', 'Testtwo', 'testthree']


def user_select_letter():
    """
    Get letter input from the user.
    """
    while True:
        print("Please Select a letter\n")

        user_input = input("Enter letter here: ")

        if validate_user_input(user_input):
            print("Test print valid data")
            break

    return user_input


def validate_user_input(user_input):
    """
    Validates user input, one letter accepted.
    """
    if user_input.isalpha() == False or len(user_input) != 1:
        print("Invalid Input\n")


letter_selected = user_select_letter()