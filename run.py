# Allows random number generation
import random

# ASCII art for lives, from https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
HANGMAN_PICTURES = ['''
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

words_list = ['testone', 'Testtwo', 'testthree', 'testfour', 'testfive']
guesses = []
lives = 6
word_index = random.randint(0, len(words_list)-1)
selected_word = words_list[word_index].upper()
print(selected_word)


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
    Validates user input, only one letter accepted.
    """
    if user_input.isalpha() == False or len(user_input) != 1:
        print("Invalid Input\n")


def print_hangman_state():
    """
    Shows the user the hangman, letters selected and correct guesses
    """
    print(HANGMAN_PICTURES[(6-lives)])
    print(f"\nYou have {lives} lives remaining!")


letter_selected = user_select_letter()