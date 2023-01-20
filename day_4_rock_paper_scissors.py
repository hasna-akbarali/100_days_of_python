import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

option = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. "))

game_images = [rock,paper,scissors]

if(option == 0 or option == 1 or option == 2):
  print(game_images[option])
else:
  print("Wrong Input! Type 0 for Rock, 1 for Paper, 2 for Scissors")

computer_option = random.randint(0,2)

print("Computer chose:")

print(game_images[computer_option])
if((option == 0 and computer_option == 2) or (option == 0 and computer_option == 2) or (option == 1 and computer_option == 0)) :
  print("You Won!")
elif(option == computer_option):
  print("Draw!")
else:
  print("You Lost!")
