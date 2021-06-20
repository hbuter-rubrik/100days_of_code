#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random
print(logo)

# get random number between 1 - 100
random_number = random.randint(1,100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Set user difficulties & attempts
user_difficulty = input("Choose difficulty. Type 'easy' or 'hard': ").lower()
if user_difficulty == "easy":
  user_attempts = 10
else:
  user_attempts = 5
print(f"you have {user_attempts} remaining to guess the number")

game_over = False

def decrease_attempts():
  return user_attempts - 1

def make_guess():
  global user_attempts
  global game_over
  if user_attempts == 0:
    print("No more attempts left, Game Over")
    game_over = True
  else: 
    guess = int(input("Make a guess: "))
    if guess > random_number:
      print("Too high\nGuess again.")
      user_attempts = decrease_attempts()
      print(f"you have {user_attempts} remaining to guess the number")
    elif guess < random_number:
      print("Too low\nGuess again.")
      user_attempts = decrease_attempts()
      print(f"you have {user_attempts} remaining to guess the number")
    elif guess == random_number:
      print("You guessed it, you win")
      game_over = True

while not game_over:
  make_guess()
