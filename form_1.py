import tkinter as tk
from tkinter import ttk
from helpers.widgets import tkInput, tkLabel, tkTable, addRowToTkTable
# from helpers.destroy_frame import destroyFrame
from phase_1 import select_all_countries, select_all_cities
import sqlite3



class PhaseOneForm:
        
    def destroyFrame(form):
        # clear the window so you can render new widgets
        if len(form.winfo_children()) > 0:
            for widget in form.winfo_children():
                widget.destroy()
            
    def form1(self, window, form):
        # destroy_frame_instance = DestroyFrame()
        # self.destroyFrame(window)
        # self.destroyFrame(form)
        if len(form.winfo_children()) > 0:
            for widget in form.winfo_children():
                widget.destroy()
            
        tkLabel(window, text="This tab shows Phase One of the project. Click any of the buttons below to get started", x=135, y=20)

        tk.Button(window, text= "Select all countries", command=lambda: self.showAllCountries(form)).place(x=25, y=60)
        tk.Button(window, text= "Select all cities", command=lambda: self.showAllCities(form)).place(x=180, y=60)
        
        
        
    def showAllCountries(self, form):
        with sqlite3.connect("db/CIS4044-N-SDI-OPENMETEO-PARTIAL.db") as connection:
            if len(form.winfo_children()) > 0:
                for widget in form.winfo_children():
                    widget.destroy()
                    
            allCountries = select_all_countries(connection, False)
            table = tkTable(form, ["Country Id", "Country Name", "Country Timezone"], 25, 100)

            for row in allCountries:
                addRowToTkTable(table, row['id'], row['name'], row['timezone'])
                
    def showAllCities(self, form):
        with sqlite3.connect("db/CIS4044-N-SDI-OPENMETEO-PARTIAL.db") as connection:
            # destroy_frame_instance = DestroyFrame()
            if len(form.winfo_children()) > 0:
                for widget in form.winfo_children():
                    widget.destroy()
            
            allCities = select_all_cities(connection, False)
            table = tkTable(form, ["City Id", "City Name", "Longitude", "Latitude", "Country ID"], 25, 100)

            for row in allCities:
                addRowToTkTable(table, row['id'], row['name'], row['longitude'], row['latitude'], row['country_id'])