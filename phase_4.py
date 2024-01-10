from helpers.widgets import tk_input, tk_label, add_placeholder, tk_checkbox, show_loader, close_loader
import tkinter as tk
from helpers.utils import db_crud, check_and_add_column, database_connection, make_request
from tkinter import messagebox

class PhaseFourForm:
    def __init__(self):    
        self.connection =  database_connection()
            
        check_and_add_column(self.connection, 'daily_weather_entries', 'daylight_duration', 'Decimal')
        check_and_add_column(self.connection, 'da