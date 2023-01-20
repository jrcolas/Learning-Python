import pandas
import random
from tkinter import *
from tkinter import ttk

BACKGROUND_COLOR = "#B1DDC6"


# ------------------------------------------ PICK RANDOM WORD --------------------------------------------- #
data = pandas.read_csv("./data/french_words.csv")
df = pandas.DataFrame(data).to_dict(orient="records")
#print(df)


def random_word():
    random_pick = random.choice(df)
    french = random_pick["French"]
    english = random_pick["English"]
    labels_front(french)


def labels_front(word):
    canvas_front.delete("word_lbl")
    canvas_front.delete("title_lbl")
    canvas_front.create_text((400, 150), text="French", font=("Arial", 40, "italic"), tags="title_lbl")
    canvas_front.create_text((400, 283), text=word, font=("Arial", 60, "bold"), tags="word_lbl")

# random_word()


# ---------------------------------------------- UI SETUP ------------------------------------------------- #
window = Tk()
window.title("Flashy")
window.config(width=800, height=526, bg=BACKGROUND_COLOR, padx=50, pady=50)

# Images
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")

canvas_front = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_front.grid(column=0, row=0, columnspan=2)
canvas_front.create_image(400, 263, image=card_front_img)
canvas_front.create_text((400, 150), text="Title", font=("Arial", 40, "italic"), tags="title_lbl")
canvas_front.create_text((400, 283), text="Word", font=("Arial", 60, "bold"), tags="word_lbl")


# Buttons
wrong_btn = Button(image=wrong_img, highlightthickness=0, bd=0)
wrong_btn.config(command=random_word)
wrong_btn.grid(column=0, row=1)

right_btn = Button(image=right_img, highlightthickness=0, bd=0)
right_btn.config(command=random_word)
right_btn.grid(column=1, row=1)


window.mainloop()
