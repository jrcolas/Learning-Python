# A simple GUI in Python

# Import GUI libraries
from Tkinter import *

# Create the window
root = Tk()

# Modify root window
root.title("My Python GUI")
root.geometry("250x125")

## Get stuff in the window
app = Frame(root)
app.grid()

## Create a label
label = Label(app, text = "My first GUI window in Python!")
label.grid()

## Create buttons
button1 = Button(app, text = "A Button!")
button1.grid()

button2 = Button(app)
button2.grid()
button2.configure(text = "Another button")

button3 = Button(app)
button3.grid()
button3["text"] = "Button 3 text!"

# Kick off the event loop
root.mainloop()
