'''
Start

Generate random word
Generate as many blank spaces as letters in the word

while missing letters
    guess a letter
        if letter is in word, fill in letter
        if letter is not in word, add a part of the man
    Go back to start

'''
import random

title_art = """ _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       \n"""

hangman = []

hangman.append( """  ________
 |      |
        |
        |
        |
        |
________|_______
|______________|""")

hangman.append("""  ________
 |      |
 O      |
        |
        |
        |
________|_______
|______________|""")

hangman.append("""  ________
 |      |
 O      |
 |      |
 |      |
        |
________|_______
|______________|""")

hangman.append("""  ________
 |      |
 O      |
/|      |
 |      |
        |
________|_______
|______________|""")

hangman.append("""  ________
 |      |
 O      |
/|\     |
 |      |
        |
________|_______
|______________|""")

hangman.append("""  ________
 |      |
 O      |
/|\     |
 |      |
/       |
________|_______
|______________|""")

hangman.append(""" ________
 |      |
 O      |
/|\     |
 |      |
/ \     |
________|_______
|______________|
""")
   


word_list = ["aardvark", "baboon", "camel"]

#i = random.randint(0,len(word_list) - 1)
chosen_word = random.choice(word_list)

charList = []
display = [] 

for letter in chosen_word:
    charList.append(letter)
    display += "_"

strikes = 6
print(title_art)
print("\n")

print(f"{display}\n")

guesses = len(charList)


while guesses != 0 and strikes != 0:
    index = 0
    spaces = ""

    print(hangman[6 - strikes])

    guessedLetter = input("Guess a letter: ").lower()
    correctGuess = 0

    for letter in charList:
        if guessedLetter == letter:
            display[index] = letter
            guesses -= 1
            correctGuess = 1
        index += 1

    if correctGuess == 0:
        strikes -= 1
        
    for stuff in display:
        spaces += stuff

    print(spaces)