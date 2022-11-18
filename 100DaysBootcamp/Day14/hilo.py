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

from art import logo
from art import vs
from game_data import data

import os

################# Start Screen #########################
print(logo)

print("Compare A: choice A, choice A description, from choice A country.")
print(vs)
print("Against B: Choice B, choice B Description, from choice B Country")
input("Who has more followers? Type 'A' or 'B': ").lower()

###################### Win Screen ######################## 
os.system('cls')

print(logo)
print("You're right! Current score is {score}")

print("Compare A: wonChoiceA, choice A description, from choice A country.")
print(vs)
print("Against B: wonChoiceB, choice B Description, from choice B Country")
input("Who has more followers? Type 'A' or 'B': ").lower()

###################### Loss Screen ######################## 
print(logo)
print("Sorry, that's wrong. Final score: {score}")