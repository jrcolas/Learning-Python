# Print the logo at the start of the game

# Ask the user to compare a random choice A from another random choice B

# Once they type A or B, clear the screen, reprint the logo and underneath that,
    # if they guessed wrong, 
        # tell them they guessed wrong
        # print the score
        # end the game.
    # if they guessed right
        # Tell them they guessed right, and print their current score (increment by 1)
        # Compare the correct choice from the previous prompt with a new random selection.
            # Not said, but make it so that the same selection isn't selected for A and B

# The game will not end until they guessed it wrong.

from unicodedata import name
from art import logo
from art import vs
from game_data import data

import os
import random

################# Start Screen #########################
print(logo)

choice_a = random.choice(data)
choice_b = random.choice(data)

# print(choice_a["name"])

print(f"Compare A: {choice_a['name']}, {choice_a['description']}, from {choice_a['country']}.")
print(vs)
print(f"Against B: {choice_b['name']}, {choice_b['description']}, from {choice_b['country']}")
answer = input("Who has more followers? Type 'A' or 'B': ").lower()

if answer == "a":
    print("Something")
elif answer == "b":
    print("something else")
else:
    print("Messed up again!")

# for entry in data:
#     print(entry["name"])

# ###################### Win Screen ######################## 
# os.system('clear')

# print(logo)
# print("You're right! Current score is {score}")

# print("Compare A: wonChoiceA, choice A description, from choice A country.")
# print(vs)
# print("Against B: wonChoiceB, choice B Description, from choice B Country")
# input("Who has more followers? Type 'A' or 'B': ").lower()

# ###################### Loss Screen ######################## 
# os.system('clear')

# print(logo)
# print("Sorry, that's wrong. Final score: {score}")