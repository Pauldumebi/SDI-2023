from tkinter import *
from tkinter import ttk

# class Widgets:
def onEntryClick(event, entry):
    if entry.get() == "Enter Text":
        entry.delete(0, "end")
        entry.config(fg='black')


def tkInput(window, text, x, y):
    # placeholder_text = "Enter Country to search"
    input = Entry(window, text=text, font=("Arial", 15))
    # input.insert(0, placeholder_text)
    # input.bind("<FocusIn>", lambda event, entry=input: on_entry_click(event, entry))

    input.place(x=x, y=y)
    
    return input


def tkLabel(window, text, x, y):
    label = Label(window, text=text, font=("Arial", 15))
    label.place(x=x, y=y)
    
    return label

def tkTable(window, columns, x, y):
    tree = ttk.Treeview(window, columns=columns)
    
    for row in columns:
        tree.heading(row, text=row)
        tree.column("#0", width=0)
        tree.column(row, width=150)
    
    tree.place(x=x, y=y)
    
    return tree
    
def addRowToTkTable(tree, *row):
    print(row, 'row')
    start = row[0]
    tree.insert("", start, values=row)

