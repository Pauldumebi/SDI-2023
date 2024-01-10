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
       