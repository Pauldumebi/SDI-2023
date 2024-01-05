import tkinter as tk
from tkinter import ttk
from helpers.widgets import tk_label, tk_options, tk_label, tk_table, add_row_to_tk_table, tk_options, tk_date_entry
from helpers.utils import get_cities
# from helpers.destroy_frame import destroyFrame
from phase_1 import select_all_countries, select_all_cities, average_annual_temperature, average_seven_day_precipitation, average_mean_temp_by_city, average_annual_precipitation_by_country
import sqlite3
from tkinter import messagebox
from  datetime import date

class PhaseOneForm:
            
    def form1(self, window, form):
        # destroy_frame_instance = DestroyFrame()
        # self.destroyFrame(window)
        # self.destroyFrame(form)
        if len(form.winfo_children()) > 0:
            for widget in form.winfo_children():
                widget.destroy()
            
        tk_label(window, text="This tab shows Phase One of the project. Click any of the buttons below to get started", x=135, y=20)

        tk.Button(window, text= "Show all countries", command=lambda: self.showAllCountries(form)).place(x=100, y=60)
        tk.Button(window, text= "Show all cities", command=lambda: self.showAllCities(form)).place(x=255, y=60)
        tk.Button(window, text= "Average annual temperature", command=lambda: self.showAvgAnnualTemp(form)).place(x=390, y=60)
        tk.Button(window, text= "Average 7days precipitation", command=lambda: self.show_avg_7_day_precipitation(form)).place(x=600, y=60)
        tk.Button(window, text= "Average mean temp by city", command=lambda: self.showAvgMeanTempByCity(form)).place(x=200, y=100)
        tk.Button(window, text= "Average annual precipitation temp by city", command=lambda: self.show_avg_annual_precipitation(form)).place(x=410, y=100)
        
        
       
        
        # city_id = int(input("City number between 1 to 4: "))
        # date_from = input("Start date (YYYY-MM-DD): ")
        # date_to = input("End date (YYYY-MM-DD): ")
        # average_mean_temp_by_city(connection, date_from, date_to)
        # year = int(input("Year from 2020 - 2022: "))
        # average_annual_precipitation_by_country(connection, year)
        
        
        
        
    def showAllCountries(self, form):
        with sqlite3.connect("db/CIS4044-N-SDI-OPENMETEO-PARTIAL.db") as connection:
            if len(form.winfo_children()) > 0:
                for widget in form.winfo_children():
                    widget.destroy()
                    
            allCountries = select_all_countries(connection, False)
            table = tk_table(form, ["Country Id", "Country Name", "Country Timezone"], 25, 100)

            for row in allCountries:
                add_row_to_tk_table(table, row['id'], row['name'], row['timezone'])
                
    def showAllCities(self, form):
        with sqlite3.connect("db/CIS4044-N-SDI-OPENMETEO-PARTIAL.db") as connection:
            # destroy_frame_instance = DestroyFrame()
            if len(form.winfo_children()) > 0:
                for widget in form.winfo_children():
                    widget.destroy()
                    
            allCities = select_all_cities(connection, False)
            table = tk_table(form, ["City Id", "City Name", "Longitude", "Latitude", "Country ID"], 25, 100)

            for row in allCities:
                add_row_to_tk_table(table, row['id'], row['name'], row['longitude'], row['latitude'], row['country_id'])
        
    def cal_avg_temp(self, display, connection, cities, city, year):
        if len(display.winfo_children()) > 0:
                for widget in display.winfo_children():
                    widget.destroy()
        
        city_id = cities[city]
        results = average_annual_temperature(connection, city_id, year, False)
        
        for row in results:
            text = f"Average annual temperature for city {row['name']} in year {year} was {row[0]:.2f}°C"
            tk_label(display, text=text, x=0, y=0)
    
    def showAvgAnnualTemp(self, form):
        try:
            with sqlite3.connect("db/CIS4044-N-SDI-OPENMETEO-PARTIAL.db") as connection:
                if len(form.winfo_children()) > 0:
                    for widget in form.winfo_children():
                        widget.destroy()
                
                cities = get_cities(connection)
                selected_value = tk.StringVar(form)
                selected_value.set(list(cities)[0])
                
                tk_label(form, text="Select a City", x=150, y=140)
                tk_options(form, selected_value, get_cities(connection).keys(), x=150, y=170)
                
                yearOption = [2020, 2021, 2022]
                year = tk.StringVar(form)
                year.set(yearOption[0])
                tk_label(form, text="Select a Year", x=300, y=140)
                tk_options(form, year, yearOption, x=300, y=170)
                
                display = tk.Frame(form, width=900, height=400)
                display.place(x=200, y=300)
                
                func = lambda: self.calAvgTemp(
                    display,
                    connection,
                    cities,
                    selected_value.get(),
                    year.get(),
                )
                
                tk.Button(form, text= "Submit", command=func).place(x=450, y=155)
        except sqlite3.Error as e:
            messagebox.showinfo(
                "showinfo", "Unable to connect to the database {e}"
            )
    
    def show_avg_7_day_precipitation(self, form):
        with sqlite3.connect("db/CIS4044-N-SDI-OPENMETEO-PARTIAL.db") as connection:
            if len(form.winfo_children()) > 0:
                for widget in form.winfo_children():
                    widget.destroy()
                    
            # city_id = int(input("City number between 1 to 4: "))
            cities = get_cities(connection)
            selected_value = tk.StringVar(form)
            selected_value.set(list(cities)[0])
            
            tk_label(form, text="Select a City", x=250, y=140)
            tk_options(form, selected_value, get_cities(connection).keys(), x=250, y=170)
            
            tk_label(form, text="Select a start date", x=450, y=140)
            date_month = tk_date_entry(form, 450, 170, min_date=date(2020, 1, 1), max_date=date(2022, 12, 31))
                
            # start_date = input("Start date (YYYY-MM-DD): ")Do you remember that yeah you don't honestly
            # average_seven_day_precipitation(connection, city_id, start_date)
        
    # def showAvgMeanTempByCity(self, form):
    #     print('Hey')
    
    
    def cal_avg_annual_precipitation(self, form, connection, year):  
        results = average_annual_precipitation_by_country(connection, year, False)
        
        for row in results:
            text = f"Average annual temperature for city {row['name']} in year {year} was {row[0]:.2f}°C"
            tk_label(form, text=text, x=0, y=0)
    
    
    def show_avg_annual_precipitation(self, form):
        try:
            with sqlite3.connect("db/CIS4044-N-SDI-OPENMETEO-PARTIAL.db") as connection:
                
                if len(form.winfo_children()) > 0:
                    for widget in form.winfo_children():
                        widget.destroy()
                        
                yearOption = [2020, 2021, 2022]
                year = tk.StringVar(form)
                year.set(yearOption[0])
                tk_label(form, text="Select a Year", x=300, y=140)
                tk_options(form, year, yearOption, x=300, y=170)
                
                func = lambda: self.cal_avg_annual_precipitation(
                    connection,
                    form,
                    year.get(),
                )
                tk.Button(form, text= "Submit", command=func).place(x=450, y=155)
                        
        except sqlite3.Error as e:
                    messagebox.showinfo(
                        "showinfo", "Unable to connect to the database {e}"
                    )
        
    # def avgAnnualPrecipitationByCountry(self, form):
    #     print('Hey')
    