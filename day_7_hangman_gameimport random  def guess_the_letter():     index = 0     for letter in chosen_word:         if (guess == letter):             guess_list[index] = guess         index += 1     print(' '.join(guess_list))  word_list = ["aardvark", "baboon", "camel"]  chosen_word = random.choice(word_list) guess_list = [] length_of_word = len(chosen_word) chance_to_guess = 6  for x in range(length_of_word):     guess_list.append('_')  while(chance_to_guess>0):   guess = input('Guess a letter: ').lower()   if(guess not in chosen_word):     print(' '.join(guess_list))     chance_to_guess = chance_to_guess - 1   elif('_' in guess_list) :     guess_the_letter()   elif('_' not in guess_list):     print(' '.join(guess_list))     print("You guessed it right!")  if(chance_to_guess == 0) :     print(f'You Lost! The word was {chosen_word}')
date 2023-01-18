# Write a program to replicate the hangman game

import random

def guess_the_letter():
    index = 0
    for letter in chosen_word:
        if (guess == letter):
            guess_list[index] = guess
        index += 1
    print(' '.join(guess_list))

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
guess_list = []
length_of_word = len(chosen_word)
chance_to_guess = 6

for x in range(length_of_word):
    guess_list.append('_')

while(chance_to_guess>0):
  guess = input('Guess a letter: ').lower()
  if(guess not in chosen_word):
    print(' '.join(guess_list))
    chance_to_guess = chance_to_guess - 1
  elif('_' in guess_list) :
    guess_the_letter()
  elif('_' not in guess_list):
    print(' '.join(guess_list))
    print("You guessed it right!")

if(chance_to_guess == 0) :
    print(f'You Lost! The word was {chosen_word}')
