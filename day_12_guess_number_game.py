import random

def compare(guess_no,num):
  global guess
  global win_flag
  if(guess_no < num):
    print('Too Low!')
    guess -= 1
    if(guess) :
      print('Guess Again!')
  elif(guess_no > num):
    print('Too High!')
    guess -= 1
    if(guess) :
      print('Guess Again!')
  else:
    win_flag = True
    print(f'You got it right! {guess_no} is correct!')
  
def guess_again():
  while  guess > 0 and win_flag == False:
    print(f'You have {guess} attempts remaining to guess the number.')
    guess_no = int(input('Make a guess: '))
    compare(guess_no,num)
  if(guess == 0 and win_flag == False):
    print("You've ran out of guesses! You Lose!")
    

print('Welcome to the number guessing game!')
print('''  ___  _  _  ____  ____  ____  __  __ _   ___     ___   __   _  _  ____ 
 / __)/ )( \(  __)/ ___)/ ___)(  )(  ( \ / __)   / __) / _\ ( \/ )(  __)
( (_ \) \/ ( ) _) \___ \\___ \ )( /    /( (_ \  ( (_ \/    \/ \/ \ ) _) 
 \___/\____/(____)(____/(____/(__)\_)__) \___/   \___/\_/\_/\_)(_/(____)''')
num = random.randint(1,100)
print('I am thinking of a number between 1 and 100. ')

level = input("Choose a difficulty. Type 'easy' or 'hard': ")
guess = 10 if(level=='easy') else 5
win_flag = False
guess_again()
