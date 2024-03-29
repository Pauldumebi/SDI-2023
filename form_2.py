import tkinter as tk
from helpers.widgets import tk_label, tk_options, tk_date_entry
from phase_2 import plot_average_temperature_cities, plot_annual_precipitation_by_country, plot_seven_day_precipitation, plot_grouped_bar_chart, plot_daily_temperature, plot_daylight_duration
from helpers.utils import get_place, months_dict, is_valid_date, database_connection
import sqlite3
from  datetime import date

class PhaseTwoForm:
    
    def __init__(self):
        self.connection =  database_connection()
        
    def seven_day_prep(self, cities, city, date):
        city_id = cities[city]
        date_valid = is_valid_date(date)
        
        if date_valid:
            plot_seven_day_precipitation(self.connection, city_id, date_valid)
            
            
    def form2(self, form):
        tk_label(form, text="This tab shows Phase Two of the project. Click any of the buttons below to get started", x=100, y=0)
        
        if(self.connection is not None):
        
            yearOption = [2020, 2021, 2022]
            
            year = tk.StringVar(form)
            year.set(yearOption[0])
            tk_label(form, text="Select a Year: ", x=100, y=70)
            tk_options(form, year, yearOption, x=200, y=70)
            
            func = lambda: plot_average_temperature_cities(
                self.connection,
                year.get() + "-01-01",
                year.get() + "-12-31",
            )
            
            tk.Button(form, text= "Show Average Annual Temperature of Cities", command=func).place(x=330, y=66)
            
            y2 = 150
            
            year_avg_temp = tk.StringVar(form)
            year_avg_temp.set(yearOption[1])
            tk_label(form, text="Select Year: ", x=100, y=y2)
            tk_options(form, year_avg_temp, yearOption, x=200, y=y2)
            
            func2 = lambda: plot_annual_precipitation_by_country(
                self.connection,
                year_avg_temp.get()
            )
            
            tk.Button(form, text= "Show Average Annual Precipitation of Countries", command=func2).place(x=330, y=y2-4)
            
            y3 = 250
            
            tk_label(form, text="Select a Start Date: ", x=5, y=y3)
            calendar = tk_date_entry(form, 140, y3, min_date=date(2020, 1, 1), max_date=date(2022, 12, 31))
            
            cities = get_place(self.connection)
            selected_value = tk.StringVar(form)
            default_city = list(cities)[0] if cities else ''
            selected_value.set(default_city)
            options = cities.keys() if cities else []
            tk_label(form, text="Select a City: ", x=325, y=y3)
            tk_options(form, selected_value, options, x=420, y=y3)
            
            func3 = lambda: self.seven_day_prep (
                cities,
                selected_value.get(),
                calendar.get()
            )
            
            tk.Button(form, text= "Show 7-Day Precipitation by City", command=func3).place(x=590, y=y3-4)
            
            y4 = 350
            
            year_avg_temp_prep = tk.StringVar(form)
            year_avg_temp_prep.set(yearOption[2])
            tk_label(form, text="Select Year: ", x=0, y=y4)
            tk_options(form, year_avg_temp_prep, yearOption, x=100, y=y4)
            
            selected_value = tk.StringVar(form)
            default_city = list(cities)[0] if cities else ''
            selected_value.set(default_city)
        
            options = cities.keys() if cities else []    
            tk_label(form, text="Select a City: ", x=200, y=y4)
            tk_options(form, selected_value, options, x=300, y=y4)
            
            func4 = lambda: plot_grouped_bar_chart(
                self.connection,
                year_avg_temp_prep.get() + "-01-01",
                year_avg_temp_prep.get() + "-12-31",
                {'id': cities[selected_value.get()], 'name': selected_value.get()},
                False
            )
            
            tk.Button(form, text= "Show Average Annual Temperature and Precipitation", command=func4).place(x=450, y=y4-4)
            
            y5 = 450
            
            year_daily_temp = tk.StringVar(form)
            year_daily_temp.set(yearOption[0])
            tk_label(form, text="Select Year: ", x=0, y=y5)
            tk_options(form, year_daily_temp, yearOption, x=90, y=y5)
            
            months = months_dict()
            selected_month = tk.StringVar(form)
            selected_month.set(list(months)[0])
            
            tk_label(form, text="Select Month: ", x=190, y=y5)
            tk_options(form, selected_month, months.keys(), x=290, y=y5)
            
            selected_city = tk.StringVar(form)
            selected_city.set(default_city)
            
            tk_label(form, text="Select a City: ", x=400, y=y5)
            tk_options(form, selected_city, options, x=500, y=y5)
            
            func5 = lambda: plot_daily_temperature(
                self.connection, 
                cities[selected_city.get()], 
                year_dail