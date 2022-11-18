import os
from art import logo


#### Functions
bids = []

def entries(bidder_name, bid_amount):
    bidder = {}
    bidder["name"] = bidder_name
    bidder["bid"] = bid_amount
    
    bids.append(bidder)

def deWinner():
    winner_bid = 0
    winner_name = ""

    for stuff in bids:
        if stuff["bid"] > winner_bid:
            winner_bid = stuff["bid"]
            winner_name = stuff["name"]       

    print(f"The winner is {winner_name} with a bid of ${winner_bid}.")


#### Main program

print(logo)
print("Welcome to the secret aution program.")

moreBidders = True
while moreBidders == True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    entries(name, bid)

    moreBid = input("Are there any other bidders? Type 'yes' or 'no' \n").lower()
    if moreBid == "no":
        os.system('cls')
        moreBidders = False
        deWinner()
    else:
        os.system('cls')
