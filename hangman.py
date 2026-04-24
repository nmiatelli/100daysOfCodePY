
import random

stages = ['''
+---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
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
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''',]

wordlist = ["music", "banana", "flowchart", "chicken", "elephant"]
lives = 6

chosen_word = random.choice(wordlist)
print (chosen_word)

placeholder = " "

for position in range (0, len(chosen_word)):
    placeholder += "_ "
print(placeholder)
    
game_over = False
correct_letters = []

while not game_over:

    guess = input("Guess a letter: ").lower()

    display = " "

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter            
        else:
            display += " _ "

    print(display)

    if guess not in chosen_word:
        lives -= 1 
        if lives == 0:
            game_over = True
            print("You looose!")

    if " _ " not in display:
        game_over = True
        print("You win!") 

    print(stages[lives])