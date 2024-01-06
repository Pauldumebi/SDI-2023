
import sqlite3
from multiprocessing import connection
from  datetime import datetime
from tkinter import messagebox


def get_cities(connection):
    
    with sqlite3.connect("db/CIS4044-N-SDI-OPENMETEO-PARTIAL.db") as connection:
        try:
            connection.row_factory = sqlite3.Row
            query = f"""
                SELECT id, name
                FROM cities
            """
            cursor = connection.cursor()
            results = cursor.execute(query)
            
            dict = {}
            
            for row in results:
                dict[row['name']] = row['id']
            
            return dict

        except sqlite3.OperationalError as ex:
            print(ex)


def destroy_window(window):
    if len(window.winfo_children()) > 0:
        for widget in window.winfo_children():
            widget.destroy()
            
            
def is_valid_date(date_str):    
    try:
        parsed_date = datetime.strptime(date_str, '%d-%m-%Y')
        formatted_date = parsed_date.strftime('%Y-%m-%d')
        
        return formatted_date
    except ValueError:
        messagebox.showerror("Error", f"The date {date_str} is not in the correct format ('dd-mm-yyyy').")
        
def months_dict():

    return {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12,
    }