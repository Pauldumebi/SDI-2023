import tkinter as tk
from tkinter import ttk
from helpers.widgets import tk_label, tk_options, tk_label, tk_table, add_row_to_tk_table, tk_options, tk_date_entry
from helpers.utils import get_place, destroy_window, is_valid_date, database_connection
from phase_1 import select_all_countries, select_all_cities, average_annual_temperature, average_seven_day_precipitation, average_mean_temp_by_city, average_annual_precipitation_by_country
from  datetime import date

class PhaseOneForm:
    def __init__(self):    
        self.connection =  database_connection()
        
    def form1(self, window, form):
        destroy_window(form)
            
        tk_label(window, text="This tab shows Phase One of the project. Click any of the buttons below to get started", x=200, y=20)

        tk.Button(window, text= "Show all countries", command=lambda: self.show_all_countries(form)).place(x=130, y=70)
        tk.Button(window, text= "Show all cities", command=lambda: self.show_all_cities(form)).place(x=290, y=70)
        tk.Button(window, text= "Average annual temperature", command=lambda: self.show_avg_annual_temp(form)).place(x=415, y=70)
        tk.Button(window, text= "Average 7days precipitation", command=lambda: self.show_avg_7_day_precipitation(form)).place(x=635, y=70)
        tk.Button(window, text= "Average mean temp by city", command=lambda: self.show_avg_mean_temp_by_city(form)).place(x=235, y=110)
        tk.Button(window, text= "Average annual precipitation temp by city", command=lambda: self.show_avg_annual_precipitation(form)).place(x=445, y=110)
        
        
    def show_all_countries(self, form):
        
        destroy_window(form)
                
        allCountries = select_all_countries(self.connection, False)
        table = tk_table(form, ["Country Id", "Country Name", "Country Timezone"], 25, 150)

        for row in allCountries:
            add_row_to_tk_table(table, row['id'], row['name'], row['timezone'])
                
                
    def show_all_cities(self, form):
        
        destroy_window(form)
                
        allCities = select_all_cities(self.connection, False)
        table = tk_table(form, ["City Id", "City Name", "Longitude", "Latitude", "Country ID"], 25, 150)

        for row in allCities:
            add_row_to_tk_table(table, row['id'], row['name'], row['longitude'], row['latitude'], row['country_id'])
                
        
    def cal_avg_temp(self, display, cities, city, year):
        destroy_window(display)
        
        city_id = cities[city]
        results = average_annual_temperature(self.connection, 