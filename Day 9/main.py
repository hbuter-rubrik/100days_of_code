from clearscreen import clear
#HINT: You can call clear() to clear the output in the console.
#print logo
import art
print(art.logo)
print("Welcome to the secret auction program")

#create dictionary for end_auction
auction = {}

should_end = True
while should_end:
  #ask username and bid
  username = input("What is your name?: ")
  price = float(input("What is your bid price?: $"))
  auction[username] = price
  
  #do you want to add another bid
  restart = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
  if restart == "yes":
    clear()
  else:
    should_end = False
    clear()

# create function to determine the winner
def auction_winner():
  highest_bidder = ""
  high_bid = 0
  for k in auction:
    if auction[k] > high_bid:
      highest_bidder = k
      high_bid = auction[k]
  print(f"The winner is {highest_bidder} with a bid of ${high_bid}")

auction_winner()