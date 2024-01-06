from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from  datetime import date, datetime
from tkinter import messagebox

# class Widgets:

def tk_input(window, text, x, y):
    input = Entry(window, text=text, font=("Arial", 15))
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
        tree.column(row, width=180)
    
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
    cal = DateEntry(window, width= 16, date_pattern="dd-mm-y", background= "blue", foreground= "red", bd=2, year=year, month=month, day=day, mindate=min_date, maxdate=max_date
                    # , state="readonly"
                    )
    cal.place(x=x_axis,y=y_axis)
    return cal


def is_valid_date(date_str):    
    try:
        parsed_date = datetime.strptime(date_str, '%d-%m-%Y')
        formatted_date = parsed_date.strftime('%Y-%m-%d')
        
        return formatted_date
    except ValueError:
        messagebox.showerror("Error", f"The date {date_str} is not in the correct format ('dd-mm-yyyy').")