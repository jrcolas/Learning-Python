from tkinter import *
from tkinter import ttk

KM = 1.60934

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=65, pady=20)


miles_entry = ttk.Entry(width=10)
miles_label = Label(text="Miles")
equal_label = Label(text="is equal to")
result_label = Label(text="0")
km_label = Label(text="Km")
calc_button = ttk.Button()


def calculate_result():
    mile = int(miles_entry.get())
    km = mile * KM
    result_label.config(text=str(km))


miles_entry.grid(column=1, row=0)
miles_label.grid(column=2, row=0)
equal_label.grid(column=0, row=1)
result_label.grid(column=1, row=1)
km_label.grid(column=2, row=1)
calc_button.grid(column=1, row=2)

calc_button.config(text="Calculate", command=calculate_result)


window.mainloop()
