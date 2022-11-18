alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#def encrypt(text_input, shift_input):
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
# ----------------- My implementation -------------------
    # indexInAlphabet = []
    # cipherList = []
    # for letter in text_input:
    #     indexInAlphabet.append(alphabet.index(letter))

    # for eachIndex in indexInAlphabet:
    #     cipherList.append(alphabet[eachIndex + shift_input])

    # cipher_text = "".join(cipherList)

    # print(f"The encoded text is {cipher_text}")


    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
# --------------------- end my implementation ---------------------------------

# # ------------------------- ALTERNATIVE WAY ----------------------------------
#     cipher_text = ""
#     for letter in text_input:
#         position = alphabet.index(letter)
#         new_position = position + shift_input
#         # Duplicating the alphabet list instead to make this function smaller.
#         # if new_position > 25:
#         #     overflowPosition = -1
#         #     while new_position != 25:
#         #         new_position -= 1
#         #         overflowPosition += 1
#         #     new_position = overflowPosition
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
    
#     print(f"The encoded text is {cipher_text}")

# ## Decrypt function
# def decrypt(text_input, shift_input):
#     plain_text = ""
#     for letter in text_input:
#         position = alphabet.index(letter)
#         new_position = position - shift_input
#         new_letter = alphabet[new_position]
#         plain_text += new_letter
    
#     print(f"The decoded text is {plain_text}")


# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)
# else:
#     print("You entered the wrong input. Try again.")

# ----------------- COMBINING ALL THE THINGS ----------------
def caesar(direction_input, text_input, shift_input):
    position = 0
    new_position = 0
    new_word = ""

    if direction_input == "decode":
            shift_input *= -1
            
    for letter in text_input:
        position = alphabet.index(letter)        
        new_position = position + shift_input
        new_word += alphabet[new_position]
    
    print(f"The {direction_input}d text is {new_word}")


caesar(direction, text, shift)