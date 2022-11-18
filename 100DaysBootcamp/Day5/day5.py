### For loop in lists
fruits = ["apple", "oranges", "peach"]

for fruit in fruits:
  print(fruit)

### For loop with range
  
# First argument in range is the starting number, second is the endpoint, not including it, 
# so from 1 to 10, third argument is to skip the steps, printing 1, 4, 7, 10
for number in range(1, 11, 3):
  print(number)

total = 0
for number in range(1, 101):
  total += number
print(total)
