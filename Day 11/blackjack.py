############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import art
from clearscreen import clear
# from replit import clear # Use this line when using replit 
import random
# Create empty lists for user and computer plus add list of cards

# Create function to deal 2 random cards to user and computer
def deal_card():
  """Return random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

# Calculate the score of both players 
"""Calculate the score for the player and the computer """ 
def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  """Compare the scores of the player and the computer and return the outcome of the comparisation """
  if user_score == computer_score:
    return f"Draw! {art.logo_draw}"
  elif computer_score == 0:
    return f"Lose, computer has BlackJack {art.logo_lost} "
  elif user_score == 0:
    return f"Win with a BlackJack {art.logo_win} "
  elif user_score > 21:
    return f"Busted, you Lose {art.logo_lost}"
  elif computer_score > 21:
    return f"Computer is busted, you win {art.logo_win}"
  elif user_score > computer_score:
    return f"You win {art.logo_win}"
  else:
    return f"You lose {art.logo_lost}"

def play_game():
  """Play BlackJack :D """
  print(art.logo)
  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"your cards {user_cards} your score: {user_score}")
    print(f"Computer first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Would you like another card? type 'y' or 'n': ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while computer_score != 0 and computer_score <17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"Your final hand is {user_cards}, final score: {user_score}")
  print(f"Computer's final hand is {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
  clear()
  play_game()
