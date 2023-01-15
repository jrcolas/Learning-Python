from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- SEARCH PASSWORD ---------------------------------- #
def find_password():
    search_word = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            key = json.load(data_file)
            try:
                key_val = key[search_word]
                messagebox.showinfo(title=search_word,
                                    message=f"Username: {key_val['user']}\n"
                                            f"Password: {key_val['password']}")
            except KeyError:
                messagebox.showerror(title=search_word,
                                     message=f"{search_word} has not been saved yet.")
    except FileNotFoundError:
        messagebox.showerror(title=f"{search_word} not found", message=f"{search_word} has not been saved yet.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    rand_password = "".join(password_list)

    pass_entry.delete(0, END)
    pass_entry.insert(0, rand_password)
    pyperclip.copy(rand_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    user = user_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "user": user,
            "password": password,
        }
    }

    if website == "" or user == "" or len(password) == 0:
        messagebox.showerror(title="Info Missing", message="Please fill in all fields.")
    else:
        is_yes = messagebox.askyesno(title=website, message=f"Save these entries brah?\n\nEmail/User: {user} "
                               f"\nPassword: {password}")

        if is_yes:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                print("File not found. Creating new file and adding data.")
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            except json.JSONDecodeError:
                print("File is empty. Adding entry.")
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                print("File has data. Adding additional data to file.")
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                pass_entry.delete(0, END)
                website_entry.focus()

            success_lbl.config(text="Password Saved Successfully.")
            window.after(5000, reset_success_lbl)


def reset_success_lbl():
    success_lbl.config(text=" ")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("MyPass Password Manager")
window.config(padx=50, pady=20)

# Image
canvas = Canvas(width=200, height=200)
canvas.grid(column=1, row=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)

# Labels
website_lbl = Label(text="Website:")
website_lbl.grid(column=0, row=1)

user_lbl = Label(text="Email/Username:")
user_lbl.grid(column=0, row=2)

pass_lbl = Label(text="Password:")
pass_lbl.grid(column=0, row=3)

success_lbl = Label(fg="green")
success_lbl.grid(column=0, row=5, columnspan=3, pady=10)

# blank_lbl = Label()
# blank_lbl.grid(column=1, row=5)


# Entries
website_entry = ttk.Entry()
website_entry.grid(column=1, row=1, sticky="EW")
website_entry.focus()

user_entry = ttk.Entry()
user_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
user_entry.insert(END, "theguy@jrcolas.com")

pass_entry = ttk.Entry()
pass_entry.grid(column=1, row=3, sticky="EW")


# Buttons
search_btn = ttk.Button(text="Search")
search_btn.grid(column=2, row=1, sticky="EW")
search_btn.config(command=find_password)

gen_btn = ttk.Button(text="Generate Password")
gen_btn.grid(column=2, row=3)
gen_btn.config(command=generate_pass)

add_btn = ttk.Button(text="Add")
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")
add_btn.config(command=save)


window.mainloop()
