import pandas
import random
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}


# ------------------------------------------- SAVE PROGRESS ----------------------------------------------- #
'''
When the right button is clicked, remove current_card from df dictionary, then save df as "words_to_learn.csv.
Next time the program runs, it needs to check if "words_to_learn.csv" exists. If it does, open that file and 
convert it to dictionary in df. If it doesn't, read the "french_words.csv" file and proceed.

Task 1: Check if words_to_learn.csv exists. If it exists, open it and save the dictionary as df. If not,
        proceed with reading "french_words.csv"
        
Task 2: If the right button is clicked, remove "current_card" from "df", save "df" as 
        "words_to_learn.csv", execute next_card function.

Task 3: If the wrong button is clicked, execute next_card function.
'''


# Button click recognition
def right_button_click():
    global df
    # df.pop(df.index(current_card))
    df.remove(current_card)
    to_learn = pandas.DataFrame(df)
    to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ------------------------------------------ PICK RANDOM WORD --------------------------------------------- #
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
    print("File found. Opened words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
    print("Words to learn csv file does not exist. Reading French Words CSV file.")

df = data.to_dict(orient="records")


def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(df)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


# ---------------------------------------------- UI SETUP ------------------------------------------------- #
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

timer = window.after(3000, func=flip_card)

# Images
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text((400, 150), text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text((400, 283), text="", font=("Arial", 60, "bold"))

# Buttons
wrong_btn = Button(image=wrong_img, highlightthickness=0, bd=0)
wrong_btn.config(command=next_card)
wrong_btn.grid(column=0, row=1)

right_btn = Button(image=right_img, highlightthickness=0, bd=0)
right_btn.config(command=right_button_click)
right_btn.grid(column=1, row=1)


next_card()




window.mainloop()
