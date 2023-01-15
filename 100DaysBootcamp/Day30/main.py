# FileNotFound
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     value = a_dictionary["non_existent_key"]
# except FileNotFoundError:
#     open("a_file.txt", "w")
#     file.write("Some stuff")
# except KeyError as error_message:
#     print(f"The key {error_message} doesn't exist")
# else:
#     print("No exceptions at all")
#     content = file.read()
# finally:
#     raise TypeError("Made up error")
#     file.close()
#     print("File was closed")


# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# IndexError
# fruit_list = ["Apple","Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)


# Raising your own exceptions

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 10:
    raise ValueError("Human height should not be over 10 feet")

bmi = weight / height ** 2
print(bmi)
