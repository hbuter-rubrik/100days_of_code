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

#from art import logo
#from clearscreen import clear
import random

# Create empty lists for user and computer plus add list of cards
user_cards = []
computer_cards = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Create function to deal 2 random cards to user and computer
def deal_card(player):
  card1 = random.choice(cards)
  card2 = random.choice(cards)
  player += card1, card2

# Calculate the score of both players  
def calculate_score(player):
  sum = 0
  for i in player:
    sum += i
  #check for black jack!
  if sum == 21:
    sum = 0 
  if sum > 21:
    for k in player:
      if k == 11:
        player[k] = 1
        sum = sum - 10
  return sum
  
# add another card
def next_card(player):
  next_card = random.choice(cards)
  player.append(next_card)

# set variable for while loop - play_game
play_game = True
in_game = True
while play_game:
  play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
  if play == 'n':
    print("thank you for playing, good bye!")
    play_game = False
  else:
    # Deal the cards using the function  
    deal_card(player=user_cards)
    deal_card(player=computer_cards)
    while in_game:
      total_user = calculate_score(player=user_cards)
      total_computer = calculate_score(player=computer_cards)
      
      print(f"Player cards are {user_cards} which totals to {total_user} ")
      print(f"First dealer card is {computer_cards[0]} ")
            
      # Check if computer has 21
      if total_computer == 21 or total_computer == 0:
        print("Computer has blackjack, You lose!")
        in_game = False
        # Check if user has 21
      elif total_user == 21 or total_user == 0:
        print("You have black jack, You Win!")
        in_game = False
      
      another_card = input("Would you like another card? type 'y' or 'n': ").lower
      if another_card == 'y':
        next_card(player=user_cards)
      else:
        in_game = False