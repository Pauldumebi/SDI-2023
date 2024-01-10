
import sqlite3
from multiprocessing import connection
from  datetime import datetime
from tkinter import messagebox
import os


def get_place(connection, table='cities'):
    
    with sqlite3.connect("db/CIS4044-N-SDI-OPENMETEO-PARTIAL.db") as connection:
        try:
            connection.row_factory = sqlite3.Row
            query = f"""
                SELECT id, name
                FROM {table}
            """
            cursor = connection.cursor()
            results = cursor.execute(query)
            
            dict = {}
            
            for row in results:
                dict[row['name']] = row['id']
            
            return dict

        except sqlite3.OperationalError as ex:
            print(ex)
            return []


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
    
def db_crud(connection, query, values=False, operation='read'):
    
    try:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        
        if operation == 'create':
            cursor.execute(query, values)
            connection.commit()
            return cursor.lastrowid
        
        elif operation == 'read':
            results = cursor.execute(query)
            fetched_results = results.fetchall()
            return fetched_results if fetched_results else None
        
        elif operation == 'update' or operation == 'delete':
            cursor.execute(query, values)
            connection.commit()
            return cursor.rowcount  # Number of rows affected
        else:
            raise ValueError("Invalid operation. Supported operations: create, read, update, delete")

                
    except sqlite3.OperationalError as ex:
        print(ex)
        
        
def check_and_add_column(connection, table_name, column_name, column_definition):
    try:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        # Check if the column already exists
        cursor.execute(f"PRAGMA table_info({table_name})")
        existing_columns = [column[1] for column in cursor.fetchall()]

        if column_name not in existing_columns:
            # Column does not exist, so add it
            cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_definition}")
            connection.commit()
            print(f"Column {column_name} added successfully to the table {table_name}")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        
def database_connection():
    db_file_path = "db/CIS4044-N-SDI-OPENMETEO-PARTIAL.db"

    try:
        # Check if the database file exists
        if os.path.exists(db_file_path):
            db_connection = sqlite3.connect(db_file_path)
        else:
            # Handle the case where the database file doesn't exist
            messagebox.showinfo("showinfo", f"The database file '{db_file_path}' does not exist.")
            db_connection = None

    except sqlite3.Error as e:
        # Handle SQLite connection error
        messagebox.showinfo("showinfo", f"Unable to connect to the database: {e}")
        db_connection = None

    return db_connection