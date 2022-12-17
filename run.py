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
game_over_word = selected_word
input_tracker = ""
print(selected_word) #test, delete later

for i in range(len(selected_word)):
    guesses = guesses + "_"

print(guesses) #test, delete later


def print_hangman_state():
    """
    Shows the user the hangman, letters selected and correct guesses
    """
    print(HANGMAN_PICTURES[(6-lives)])
    print(f"\nYou have {lives} lives remaining!")


while lives > 0:
    print_hangman_state()
    print("===============")
    print("Please Select a letter")
    print(f"Guessed letters: {input_tracker}")
    print(guesses)
    user_input = input("Enter letter here: ").upper()
    if user_input.isalpha() == False or len(user_input) != 1:
        print("===============")
        print("Invalid Input")
        continue
    if user_input in game_over_word:
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
    if user_input in input_tracker:
        print(f"You have already guessed {user_input}!")
        continue
    input_tracker = input_tracker + user_input
    print(input_tracker)
                

#  Shows win and loss messages on game over
if lives == 0:
    print_hangman_state()
    print(f"Game Over! The word was {game_over_word}!")
else:
    print(f"Congratulations, you win! The word was {game_over_word}!")
