"""Blind Auction"""

from click import clear

biddings = {}

name = input("Enter Your name : ")
bid = int(input("What is your bid ? "))

biddings[name] = bid

while True:
    choice = input("Are there other players to bid ? Type 'y' or 'n'")
    clear()
    if choice == 'y':
        name = input("Enter your name : ")
        bid = int(input("Enter your bid : "))
        biddings[name] = bid
    else:
        break 

highest_bid = 0
winner = ""
for item in biddings:
    if highest_bid < biddings[item]:
        highest_bid = biddings[item]
        winner = item

print(f"The Highest bid is of {highest_bid} by {winner}")