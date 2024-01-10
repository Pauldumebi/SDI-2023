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
        results = average_annual_temperature(self.connection, city_id, year, False)
        
        for row in results:
            print(row, 'row')
            text = f"Average annual temperature for city {row['name']} in year {year} was {row['avg_temp']:.2f}°C"
            tk_label(display, text=text, x=0, y=0)
            
    
    def show_avg_annual_temp(self, form):
        
        destroy_window(form)
        
        cities = get_place(self.connection)
        selected_value = tk.StringVar(form)
        default_city = list(cities)[0] if cities else ''
        selected_value.set(default_city)
        
        tk_label(form, text="Select a City", x=150, y=140)
        options = cities.keys() if cities else []
        
        tk_options(form, selected_value, options, x=150, y=170)
        
        yearOption = [2020, 2021, 2022]
        year = tk.StringVar(form)
        year.set(yearOption[0])
        tk_label(form, text="Select a Year", x=300, y=140)
        tk_options(form, year, yearOption, x=300, y=170)
        
        display = tk.Frame(form, width=900, height=400)
        display.place(x=200, y=300)
        
        func = lambda: self.cal_avg_temp(
            display,
            cities,
            selected_value.get(),
            year.get(),
        )
        
        tk.Button(form, text= "Submit", command=func).place(x=450, y=155)
            
            
    def cal_avg_7_day_precipitation(self, form, cities, city, date):
        city_id = cities[city]
        date_valid = is_valid_date(date)
        
        if is_valid_date(date):
            result = average_seven_day_precipitation(self.connection, city_id, date_valid, False)
            tk_label(form, text=result[0], x=200, y=250)
            tk_label(form, text=result[1], x=300, y=300)
            
    
    def show_avg_7_day_precipitation(self, form):
        
        destroy_window(form)
                
        cities = get_place(self.connection)
        selected_value = tk.StringVar(form)
        default_city = list(cities)[0] if cities else ''
        selected_value.set(default_city)
        
        options = cities.keys() if cities else []
        tk_label(form, text="Select a City", x=250, y=140)
        tk_options(form, selected_value, options, x=250, y=170)
        
        tk_label(form, text="Select a start date", x=420, y=140)
        calendar = tk_date_entry(form, 420, 170, min_date=date(2020, 1, 1), max_date=date(2022, 12, 31))
        
        
        func = lambda: self.cal_avg_7_day_precipitation(
            form,
            cities,
            selected_value.get(),
            calendar.get()
        )
        
        tk.Button(form, text= "Submit", command=func).place(x=620, y=155)
                
        
    def cal_avg_mean_temp_by_city(self, form, date_from, date_to):
        date_from = is_valid_date(date_from)
        date_to = is_valid_date(date_to)
        
        if date_from and date_to:
            results = average_mean_temp_by_city(self.connection, date_from, date_to, False)
                
            for i, row in enumerate(results):
                text = f"Average mean temperature from {date_from} to {date_to} in {row['city_name']} is {row['avg_temperature']:.2f}"
                tk_label(form, text=text, x=200, y=250 + i * 30)
        
        
    def show_avg_mean_temp_by_city(self, form):
        
        destroy_window(form)
        tk_label(form, text="Select a start date", x=200, y=140)
        date_from = tk_date_entry(form, 200, 170, min_date=date(2020, 1, 1), max_date=date(2022, 12, 31))
        tk_label(form, text="Select a end date", x=400, y=140)
        date_to = tk_date_entry(form, 400, 170, min_date=date(2020, 1, 1), max_date=date(2022, 12, 31), year=2021,month=11,day=11)
        
        func = lambda: self.cal_avg_mean_temp_by_city(
            form,
            date_from.get(),
            date_to.get()
        )
        
        tk.Button(form, text= "Submit", command=func).place(x=630, y=150)
    
    
    def cal_avg_annual_precipitation(self, form, year):  
        results = average_annual_precipitation_by_country(self.connection, year, False)
        
        if results:
            for i, row in enumerate(results):
                text = f"Average annual precipitation for {row['country_name']} in {year}: {row['avg_precipitation']}"
                tk_label(form, text=text, x=250, y=250 + i * 30)
        else:
            text = "No data found for the specified time period."
            tk_label(form, text=text, x=250, y=300)
    
    
    def show_avg_annual_precipitation(self, form):
                
        destroy_window(form)    
        yearOption = [2020, 2021, 2022]
        year = tk.StringVar(form)
        year.set(yearOption[0])
        tk_label(form, text="Select a Year", x=300, y=140)
        tk_options(form, year, yearOption, x=300, y=170)
        
        func = lambda: self.cal_avg_annual_precipitation(
            form,
            year.get(),
        )
        tk.Button(form, text= "Submit", command=func).place(x=450, y=155)