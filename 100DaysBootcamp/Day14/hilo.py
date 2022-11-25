from art import logo, vs
from game_data import data

import os
import random


# Functions

def format_data(account):
    """Format the account data into a printable format."""
    name = account['name']
    desc = account['description']
    country = account['country']
    return f"{name}, {desc}, from {country}"


def compare_followers(guess, a, b):
    """Takes in the selected choice and the unselected choice to compare the numbers of the 
    followers each choice have. Returns a set value depending on whether the correct choice 
    made or not."""

    if a > b:
        return guess == "a"
    else:
        return guess == "b"


# Start Program
user_choice = []
current_score = 0
game_over = False
swap_account = False
choice_b = random.choice(data)

# Display art
print(logo)

while not game_over:
    choice_a = choice_b
    choice_b = random.choice(data)
    
    while choice_a == choice_b:
        choice_b = random.choice(data)
        
    # Print comparison prompt
    print(f"Compare A: {format_data(choice_a)}.")
    print(vs)
    print(f"Against B: {format_data(choice_b)}.")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if the user is correct
    ## Get follower count of each account
    a_follows = int(choice_a['follower_count'])
    b_follows = int(choice_b['follower_count'])

    ## Check if user is correct
    is_correct = compare_followers(guess, a_follows, b_follows)

    # Give user feedback on their guess
    # Score keeping
    os.system('cls')
    print(logo)

    if is_correct:
        current_score += 1
        print(f"You're right! Current score is {current_score}")
    else:
        game_over = True
        print(f"Sorry, you're wrong. Final score is {current_score}")

