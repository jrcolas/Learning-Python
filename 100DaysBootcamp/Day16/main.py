from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# Declarations
coffeemaker = CoffeeMaker()
money_machine = MoneyMachine()
coffee_menu = Menu()
maker_is_on = True

# Prompt user by asking what they would like
while maker_is_on:
    answer = input(f"What would you like? ({coffee_menu.get_items()}): ").lower()

    # Turn off the coffee machine by entering "off" to the prompt
    if answer == "off":
        maker_is_on = False
        break
    elif answer == "report":
        coffeemaker.report()
        money_machine.report()
    else:
        drink = coffee_menu.find_drink(answer)

        # Check if there's enough ingredients
        if coffeemaker.is_resource_sufficient(drink):
            # Ask to add money, if enough, make coffee
            if money_machine.make_payment(drink.cost):
                coffeemaker.make_coffee(drink)
