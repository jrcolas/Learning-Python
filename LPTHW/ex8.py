# Exercise 8: Printing, Printing

# Declared variable with 4 formatters
formatter = "%r %r %r %r"

# Prints 1 2 3 4
print formatter % (1, 2, 3, 4)

# Prints the strings
print formatter % ("one", "two", "three", "four")

# Prints the booleans
print formatter % (True, False, False, True)

# Prints the variable formatters
print formatter % (formatter, formatter, formatter, formatter)

# Prints the strings. The 3rd string will use double quotes because it already
# has a single quote in it.
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
