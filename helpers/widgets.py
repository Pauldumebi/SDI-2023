# from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from  datetime import date
import tkinter as tk

# class Widgets:
def on_entry_click(entry, placeholder_text):
        if entry.get() == placeholder_text:
            entry.delete(0, tk.END)
            entry.config(fg='black')
            
def on_focus_out(entry, placeholder_text):
    if entry.get() == "":
        entry.insert(0, placeholder_text)
        entry.config(fg='grey')

def add_placeholder(entry, placeholder_text):
    entry.insert(0, placeholder_text)
    entry.bind("<FocusIn>", lambda event: on_entry_click(entry, placeholder_text))
    entry.bind("<FocusOut>", lambda event: on_focus_out(entry, placeholder_text))

def tk_input(window, text, x, y):
    input = tk.Entry(window, text=text, font=("Arial", 15))
    input.place(x=x, y=y)
    
    return input

def tk_checkbox(window, text, var, x, y, disabled=True):
    checkbox = tk.Checkbutton(window, text=text, variable=var)
    checkbox.place(x=x, y=y)
    
    if disabled:
        checkbox.config(state="disabled")
    
    return checkbox


def tk_label(window, text, x, y):
    label = tk.Label(window, text=text, font=("Arial", 15))
    label.place(x=x, y=y)
    
    return label

def tk_table(window, columns, x, y):
    tree = ttk.Treeview(window, columns=columns)
    
    for row in columns:
        tree.heading(row, text=row)
        tree.column("#0", width=0)
        tree.column(row, width=180)
    
    tree.place(x=x, y=y)
    
    return tree
    
def add_row_to_tk_table(tree, *row):
    start = row[0]
    tree.insert("", start, values=row)

def tk_options(window, val, OPTIONS, x, y):

    dropDownMenu = tk.OptionMenu(window, val, *OPTIONS)
    dropDownMenu.place(x=x, y=y)
    
    return dropDownMenu

def tk_date_entry(window,x_axis,y_axis,min_date=date(2020,2,1), max_date=date(2022,12,31), year=2020,month=3,day=17): 
    cal = DateEntry(window, width= 16, date_pattern="dd-mm-y", background= "blue", foreground= "red", bd=2, year=year, month=month, day=day, mindate=min_date, maxdate=max_date
                    # , state="readonly"
                    )
    cal.place(x=x_axis,y=y_axis)
    return cal

def show_loader(window):
    loader_window = tk.Toplevel(window)
    loader_window.title("Loading...")

    # Create a Label with a message
    label = tk.Label(loader_window, text="Please wait...", font=("Arial", 12))
    label.pack(pady=10)

    return loader_window

def close_loader(loader_window):
    loader_window.destroy()