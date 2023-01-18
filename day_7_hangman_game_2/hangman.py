
import random
from ascii_art import logo
from ascii_art import stages
from words_list import words

#Logo for HangMan Game
print(logo)

# Check if the entered letter is present in the randomly selected word
def guess_the_letter():
    for position in range(length_of_word):
        letter = chosen_word[position]
        if (guess == letter):
            guess_list[position] = guess
    print(' '.join(guess_list))
    print(stages[chance_to_guess])    

# Choose a word randomly from words_list.py file
chosen_word = random.choice(words)

# Create an empty list for the guesses the user will make
guess_list = []

end_game = False
# Length of the word that was randomly selected
length_of_word = len(chosen_word)

# Number of chances for the user to guess
chance_to_guess = 6

for _ in range(length_of_word):
    guess_list.append('_')

while not end_game:
    guess = input('Guess a letter: ').lower()
    if (guess not in chosen_word):
        print(
            f'You guessed {guess}, that\'s not in the word. You lose a life.')
        print(' '.join(guess_list))
        chance_to_guess = chance_to_guess - 1
        if(chance_to_guess == 0):
            end_game = True
        print(stages[chance_to_guess])

    if ('_' in guess_list):
        guess_the_letter()
        
    if ('_' not in guess_list):
        end_game = True
        print(' '.join(guess_list))
        print("You guessed it right!")

if (chance_to_guess == 0):
    print(f'You Lost! The word was {chosen_word}')
