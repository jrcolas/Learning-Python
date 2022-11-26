# Start of day 15 file.
# Author: JrColas

# 1. Print report.
# 2. Check if resource is sufficient.
# 3. Process coin.
# 4. Check transaction successful.
# 5. Make coffee.


from menu import MENU, resources

# Declarations
avail_water = resources["water"]
avail_milk = resources["milk"]
avail_coffee = resources["coffee"]
total_money = 0
keep_going = True


# Functions
def money_in_machine(q, d, n, p):
    q_tot = q * 0.25
    d_tot = d * 0.10
    n_tot = n * 0.05
    p_tot = p * 0.01
    return q_tot + d_tot + n_tot + p_tot


# -------------------- START OF PROGRAM -------------------------

# Repeat the program
while keep_going:
    # Print prompt to user on what they would like
    print("------------------------------------------------------------------------")
    user_choice = input("Which coffee would you like? (espresso/latte/cappuccino): ").lower()

    # Turn off the coffee machine
    if user_choice == "off":
        keep_going = False
        break

    if user_choice == "report":
        print(f"Water: {avail_water}ml")
        print(f"Milk: {avail_milk}ml")
        print(f"Coffee: {avail_coffee}g")
        print(f"Money: ${total_money}")
    else:

        # Check if there's enough ingredients for the chosen coffee before asking for money
        if user_choice != "espresso":
            needed_milk = MENU[user_choice]['ingredients']['milk']
        needed_water = MENU[user_choice]['ingredients']['water']
        needed_coffee = MENU[user_choice]['ingredients']['coffee']

        if user_choice != "espresso":
            if avail_milk < needed_milk:
                print("Sorry there isn't enough milk.")
                keep_going = False
                break
            else:
                avail_milk -= needed_milk

        if avail_water < needed_water:
            print("Sorry there isn't enough water.")
            keep_going = False
            break
        else:
            avail_water -= needed_water

        if avail_coffee < needed_coffee:
            print("Sorry there isn't enough milk.")
            keep_going = False
            break
        else:
            avail_coffee -= needed_coffee

        # Ask the user to insert the coins
        # - Prompt each time for the number of quarters, dimes, nickels and pennies
        quarters = int(input("Number of quarters: "))
        dimes = int(input("Number of dimes: "))
        nickels = int(input("Number of nickels: "))
        pennies = int(input("Number of pennies: "))

        # Calculate the amount of money was inserted into the machine
        total_money = money_in_machine(quarters, dimes, nickels, pennies)

        # Check if enough money was given for selected choice
        # - Give the user back their change
        cost = MENU[user_choice]["cost"]
        if cost <= total_money:
            change = round(total_money - cost, 2)
            print(f"Here is {change} in change.")
            print(f"Here is your {user_choice} ☕. Enjoy!")
            total_money -= change
        else:
            print("Sorry, that's not enough money. Money refunded.")