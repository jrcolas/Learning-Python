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

# # Dictionary Comprehension
new_dict = {new_key:new_value for (key, value) in dict.items()}

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
import random
student_score = {student:random.randint(1, 100) for student in names}
passed_students = {student:score for (student, score) in student_score.items() if score >= 70}


# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Looping through a data frame
# for (key, value) in student_data_frame.items():
#     print(value)
# Loop through rows of a data frame
for(index, row) in student_data_frame.iterrows():
    print(index)
    print(row)
    print(row.student)
    print(row.score)
    if row.student == "Angela":
        print(row.score)
