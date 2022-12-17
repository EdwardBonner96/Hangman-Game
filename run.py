#  Allows random number generation
import random

"""
ASCII art for lives, from 
https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
"""
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

#  List of possible words to guess
words_list = ['Empress', 'Liable', 'Require', 'Examination', 'Medical',
     'Difficulty', 'Amazing', 'Ignore', 'Castle', 'Onomatopoeia']

guesses = ""
input_tracker = ""
lives = 6

#  Selects a random word from the words_list
word_index = random.randint(0, len(words_list)-1)
selected_word = words_list[word_index].upper()
CHOSEN_WORD = selected_word

#  Builds a number of underscores equal to word length
for i in range(len(selected_word)):
    guesses = guesses + "_"


def print_hangman_state():
    """
    Shows the user the hangman status and remaining lives
    """
    print(HANGMAN_PICTURES[(6-lives)])
    print(f"\nYou have {lives} lives remaining!")


while lives > 0:
    """
    Basic formatting and user information, tracks their chosen letters
    through the game and converts input to a capital letter
    """
    print_hangman_state()
    print("===============")
    print("Please Select a letter")
    print(f"Guessed letters: {input_tracker}")
    print(guesses)
    user_input = input(f"Enter letter here:\n").upper()

    if user_input.isalpha() is False or len(user_input) != 1:
        """
        Verifies user input is one letter and rejects invalid
        inputs, informs the user of this
        """
        print("===============")
        print("Invalid Input")
        continue

    if user_input in input_tracker:
        """
        Tracks guessed letters though the game and tells
        the user if they have already guessed a letter
        """
        print(f"You have already guessed {user_input}!")
        continue

    input_tracker = input_tracker + user_input

    if user_input in CHOSEN_WORD:
        """
        Checks the user guessed a correct letter and replaces
        the blank gaps in the word, filling them in with the letter
        """
        for i in range(0, len(selected_word)):
            if user_input == selected_word[i]:
                x = selected_word.find(user_input) 
                guesses = guesses[:x] + user_input + guesses[x+1:]
                selected_word = selected_word[:x] + "_" + selected_word[x+1:]
        if "_" not in guesses:
            break
    else:
        lives -= 1
        print(f"\nThe letter {user_input} is not in the word!")          

#  Shows win and loss messages on game over
if lives == 0:
    print_hangman_state()
    print(f"Game Over! The word was {CHOSEN_WORD}!")
else:
    print(f"Congratulations, you win! The word was {CHOSEN_WORD}!")