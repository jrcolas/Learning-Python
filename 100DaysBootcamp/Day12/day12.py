################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

### Local Scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)
'''
print(potion_strength) # will return error because potion_strength is defined inside of the drink_potion function, and not outside of it, so it doesn't know it has been declared inside the function.
'''

### Global Scope

player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health) 

drink_potion() # will print the player_health value because that is declared outside of the function, so everyone has access to it.


################# Block Scope ###############
# There is no block scope in Python
# Anything inside a if, for, while, etc do not have local scope, and variables can be called from anywhere.


############## Modifying a Global Variable #############

enemies = 1

def increase_enemies():
    global enemies

    enemies += 1 # Wont work because this variable is it's own thing, and it hasn't been defined a value inside this function. To increment the global variable of enemies, we have to declare in this function that there is a global variable called eneimies in this document by writing global enemies as seen above. To avoid confusion, this method shouldn't be used. Instead, use a return statement as follows: return enemies + 1
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


################ Global Constants ###############
# variables that you won't be changing. Usually defined as uppercase variables.