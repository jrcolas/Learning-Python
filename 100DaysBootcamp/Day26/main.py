# # List Comprehension

# new_list = [new_item for item in list]

numbers = [1, 2, 3]
# no comprehension
new_list = []
for n in numbers:
    new_item = n + 1
    new_list.append(new_item)

# comprehension
new_list = [n + 1 for n in numbers]

# # Conditional List Comprehension
# new_list = [new_item for item in list if test]

new_numbers = [n + 1 for n in numbers]
name = "Franck"
new_list = [letter for letter in name]
range(1, 5)
range(1, 5)
double_range = [n * 2 for n in range(1, 5)]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
cap_names = [name for name in names if len(name) > 5]
cap_names = [name.upper() for name in names if len(name) > 5]

