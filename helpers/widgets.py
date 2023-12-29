from tkinter import *


def on_entry_click(event, entry):
    if entry.get() == "Enter Text":
        entry.delete(0, "end")
        entry.config(fg='black')


def tkInput (window, text, x, y):
    # placeholder_text = "Enter Country to search"
    input = Entry(window, text=text, font=("Arial", 15))
    # input.insert(0, placeholder_text)
    # input.bind("<FocusIn>", lambda event, entry=input: on_entry_click(event, entry))

    input.place(x=x, y=y)
    
    return input


def tkLabel (window, text, x, y):
    label = Label(window, text=text, font=("Arial", 15))
    label.place(x=x, y=y)
    
    return label