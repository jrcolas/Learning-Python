# # # Tkinter # # #

from tkinter import *

window = Tk()
window.title("Some GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)



def button_clicked():
    the_entry = input.get()
    my_label.config(text=the_entry)


# Label
my_label = Label(text="I'm a label", font=("Arial", 18, "normal"))
# my_label.pack()
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(pady=30, padx=30)

# Button
button = Button(text="Clickity", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text="New Button")
button2.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=3, row=2)



# place()



window.mainloop()
