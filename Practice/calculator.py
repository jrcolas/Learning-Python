# Simple calculator
# Franck J Colas
# ------------------------------------------------------

# Function for addition
def addition(x, y):
    return x + y

# Function for subtraction
def subtraction(x, y):
    return x - y

# Function for multiplication
def multiplication(x, y):
    return x * y

# Function for division
def division(x, y):
    return x / y

# Starting menu
print("Welcome! What do you want to do?")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Read choice input from user
choice = input("Your choice [1/2/3/4]")

# Input values from user
firstVal = int(input("Enter first number: "))
secondVal = int(input("Enter second number: "))

# Calculations
if choice == '1':
    print(firstVal, "+", secondVal, "=", addition(firstVal, secondVal))

elif choice == '2':
    print(firstVal, "-", secondVal, "=", subtraction(firstVal, secondVal))

elif choice == '3':
    print(firstVal, "*", secondVal, "=", multiplication(firstVal, secondVal))

elif choice == '4':
    print(firstVal, "/", secondVal, "=", division(firstVal, secondVal))

else:
    print("Invalid input. Try again.")
