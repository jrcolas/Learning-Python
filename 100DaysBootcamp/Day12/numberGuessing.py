from art import logo
from random import randint
import os

EASY_GUESS = 10
HARD_GUESS = 5

randomNumber = randint(1,100)

os.system('cls')
print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
attempts = 0

def guess_game(atpt):
    '''Takes in the number of attempts left for the user to use'''
    print(f"You have {atpt} attempts remaining to guess the number.")
    user_guess = int(input("Take a guess: "))

    while user_guess != randomNumber and atpt != 1:
        if user_guess < randomNumber:
            atpt -= 1
            print("Too low.")
            print(f"You have {atpt} attempts remaining to guess the number.")
            user_guess = int(input("Take a guess: "))
        else:
            atpt -= 1
            print("Too high.")
            print(f"You have {atpt} attempts remaining to guess the number.")
            user_guess = int(input("Take a guess: "))

        if user_guess == randomNumber:
            print("Congratulations! You guessed it right!")
    
    if user_guess != randomNumber:
        print(f"You've used up all of your attempts. The number was {randomNumber}.")

if difficulty == "easy":
    attempts_left = EASY_GUESS - attempts
elif difficulty == "hard":
    attempts_left = HARD_GUESS - attempts
else:
    print("You done messed up!")

guess_game(attempts_left)

