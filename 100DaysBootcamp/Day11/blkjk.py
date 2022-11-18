from art import logo
import os
import random

def new_game():
    start = input("Welcome to BlackJack! Do you want to play a game? 'Yes' or 'No': ").lower()

    if start == "no":
        print("Goodbye!")
        return False
    else:
        return True

def deal_card():
    """Returns a random card from the deck"""
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    return random.choice(deck)

def calculate_score(cards):
    """Takes some cards as an input and returns the sum of those cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(us, cs):
    """Compares the scores to figure out the winner."""
    if us == cs:
        return "Draw"
    elif cs == 0 or us > 21:
        return "You lose."
    elif us == 0 or cs > 21:
        return "You win!"
    elif us > 21:
        return "You lose."
    elif cs > 21:
        return "You win!"
    elif us > cs:
        return "You win!"
    else:
        return "You lose."

print(logo)

while new_game():
    os.system('cls')
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"My cards are {user_cards}, with a total score of {user_score}")
        print(f"The computer's first card is {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
