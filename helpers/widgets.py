from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from  datetime import date

# class Widgets:
def onEntryClick(event, entry):
    if entry.get() == "Enter Text":
        entry.delete(0, "end")
        entry.config(fg='black')


def tk_input(window, text, x, y):
    # placeholder_text = "Enter Country to search"
    input = Entry(window, text=text, font=("Arial", 15))
    # input.insert(0, placeholder_text)
    # input.bind("<FocusIn>", lambda event, entry=input: on_entry_click(event, entry))

    input.place(x=x, y=y)
    
    return input


def tk_label(window, text, x, y):
    label = Label(window, text=text, font=("Arial", 15))
    label.place(x=x, y=y)
    
    return label

def tk_table(window, columns, x, y):
    tree = ttk.Treeview(window, columns=columns)
    
    for row in columns:
        tree.heading(row, text=row)
        tree.column("#0", width=0)
        tree.column(row, width=150)
    
    tree.place(x=x, y=y)
    
    return tree
    
def add_row_to_tk_table(tree, *row):
    start = row[0]
    tree.insert("", start, values=row)

def tk_options(window, val, OPTIONS, x, y):

    dropDownMenu = OptionMenu(window, val, *OPTIONS)
    dropDownMenu.place(x=x, y=y)
    
    return dropDownMenu

def tk_date_entry(window,x_axis,y_axis,min_date=date(2020,2,1), max_date=date(2022,12,31), year=2020,month=3,day=17): 
    cal = DateEntry(window, width= 16, date_pattern="dd-mm-y", background= "blue", foreground= "red",bd=2,year=year,month=month,day=day, mindate=min_date, maxdate=max_date
                    # , state="readonly"
                    )
    cal.place(x=x_axis,y=y_axis)
    return cal