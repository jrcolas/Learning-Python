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
import random

################# Start Screen #########################


def prompt_user(a, b):
    ### TEST PRINT STATEMENT  ###########
    print(f"Choice A: {a['follower_count']}, Choice B: {b['follower_count']}")
    ### TEST PRINT STATEMENT END  ###########
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}.")
    print(vs)
    print(f"Against B: {b['name']}, {b['description']}, from {b['country']}")

    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    return answer


user_choice = []
current_score = 0
game_over = False

print(logo)

choice_a = random.choice(data)
choice_b = random.choice(data)
    

def compare_followers(a, b):
    """Takes in the selected choice and the unselected choice to compare the numbers of the 
    followers each choice have. Returns a set value depending on whether the correct choice 
    made or not."""
    hc_follows = int(a['follower_count'])
    lc_follows = int(b['follower_count'])

    if  hc_follows > lc_follows:
        return 0 # Zero = Correct choice made
    elif hc_follows == lc_follows:
        return 1 # One = Same choice made or same number of followers
    else:
        return 2 # Two = Incorrect choice made.

prompt_answer = prompt_user(choice_a, choice_b)

while not game_over:
    higher_choice = choice_a
    lower_choice = choice_b

    while prompt_answer == "a":
        result = compare_followers(higher_choice, lower_choice)

        if result == 0:
            current_score += 1
            print(f"You're right! Current score is {current_score}")

            choice_b = random.choice(data)

            prompt_answer = prompt_user(higher_choice, choice_b)

        elif result == 1:
            current_score += 1
            print(f"That one's on us. Current score is {current_score}")
            choice_b = random.choice(data)

            prompt_answer = prompt_user(higher_choice, choice_b)    
        else:
            print(f"Sorry, that's wrong. Final score: {current_score}")
            game_over = True
            break


    while prompt_answer == "b":
        # higher_choice = choice_b
        # lower_choice = choice_a

        result = compare_followers(higher_choice, lower_choice)

        if result == 0:
            current_score += 1
            print(f"You're right! Current score is {current_score}")

            choice_b = random.choice(data)

            prompt_answer = prompt_user(higher_choice, choice_b)

        elif result == 1:
            current_score += 1
            print(f"That one's on us. Current score is {current_score}")
            choice_b = random.choice(data)

            prompt_answer = prompt_user(higher_choice, choice_b)    
        else:
            print(f"Sorry, that's wrong. Final score: {current_score}")
            game_over = True
            break
