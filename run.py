#  Allows random number generation
import random

#  ASCII art for lives, from https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
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
guesses = ""
lives = 6
word_index = random.randint(0, len(words_list)-1)
selected_word = words_list[word_index].upper()
print(selected_word) #test, delete later

for i in range(len(selected_word)):
    guesses = guesses + "_ "

print(guesses) #test, delete later


def user_select_letter():
    """
    Get letter input from the user.
    """
    print("===============")
    print("Please Select a letter")
    print(guesses)
    user_input = input("Enter letter here: ")

    return user_input


def validate_user_input(user_input):
    """
    Validates user input, only one letter accepted.
    """
    if user_input.isalpha() == False or len(user_input) != 1:
        print("===============")
        print("Invalid Input")
        print(f"{lives} lives remaining")


def print_hangman_state():
    """
    Shows the user the hangman, letters selected and correct guesses
    """
    print(HANGMAN_PICTURES[(6-lives)])
    print(f"\nYou have {lives} lives remaining!")


while lives > 0:
    print_hangman_state()
    letter_selected = user_select_letter()
    if letter_selected in selected_word:
        for i in range(len(selected_word)):
            if letter_selected == selected_word[i]:
                guesses[i] = letter_selected
        if "_" not in guesses:
            break
    else:
        lives -= 1
        print_hangman_state()
        print(f"{letter_selected} is not in the word!")
                

#  Shows win and loss messages on game over
if lives == 0:
    print_hangman_state()
    print(f"Game Over! The word was {selected_word}!")
else:
    print(f"Congratulations, you win! The word was {selected_word}!")