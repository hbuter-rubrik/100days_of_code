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

import random

# User choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n"))
# Compute Choice 
computer_choice = random.randint(0,2)

# The Game
game_list = [rock, paper, scissors]

#display what user chooses
if user_choice >= 3 or user_choice <0:
  print("You typed an invalid number, You lose!!")
else:
  print(f"Player chooses \n {game_list[user_choice]}")

  # display what computer chooses
  print(f"Computer choose: \n {game_list[computer_choice]}")

  # Game mechanics
  if user_choice == computer_choice:
    print("Its a draw")
  elif user_choice == 0 and computer_choice == 1: # rock vs paper
    print("You Lose")
  elif user_choice == 0 and computer_choice == 2: # rock vs scissors
    print("You Win")
  elif user_choice == 1 and computer_choice == 2: # paper vs scissors
    print("You Lose")
  elif user_choice == 1 and computer_choice == 0: # paper vs rock
    print("You Win") 
  elif user_choice == 2 and computer_choice == 0: # scissors vs rock
    print("You Lose")
  elif user_choice == 2 and computer_choice == 1: # scissors vs scissors
    print("You Win")

