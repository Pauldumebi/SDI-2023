from helpers.widgets import tk_input, tk_label, add_placeholder, tk_checkbox, show_loader, close_loader
import tkinter as tk
from helpers.request import make_request
from helpers.utils import db_crud, check_and_add_column, database_connection
from tkinter import messagebox

class PhaseFourForm:
    def __init__(self):    
        self.connection =  database_connection()
            
        check_and_add_column(self.connection, 'daily_weather_entries', 'daylight_duration', 'Decimal')
        check_and_add_column(self.connection, 'daily_weather_entries', 'uv_index_max', 'Decimal')
        
    def add_column(self, check_value, columns, placeholders, values, column_name, check_value_array, value_to_append_array, val, count, insert=False):
        
        if insert:
            if check_value:
                columns.append(column_name)
                placeholders.append("?") 
                values.append(value_to_append_array[val][count])
                
        if check_value in check_value_array:
            columns.append(column_name)
            placeholders.append("?")
            values.append(value_to_append_array[check_value][count])

                
    def get_city_info(self, text, minimum_temp, maximum_temp, mean_temp, precipitation_sum, daylight_duration, uv_index_max, form):
        if(text == ""):
            return messagebox.showinfo( "showinfo", "Enter a city name")
        
        values = [minimum_temp, maximum_temp, mean_temp, precipitation_sum, daylight_duration, uv_index_max]
        if(all(value == 0 for value in values)):
            return messagebox.showinfo( "showinfo", "Select at least one data to fetch")
        
        # show_loader(form)
        
        url_params = ''
        
        if(minimum_temp):
            url_params = url_params + "temperature_2m_min,"
            
        if(maximum_temp):
            url_params = url_params + "temperature_2m_max,"
            
        if(mean_temp):
            url_params = url_params + "temperature_2m_mean,"
        
        if(precipitation_sum):
            url_params = url_params + "precipitation_sum,"
            
        if(daylight_duration):
            url_params = url_params + "daylight_duration,"
            
        if(uv_index_max):
            url_params = url_params + "uv_index_max"

        # Check database to see if entry exists for the city if not fetch from API
        query_0 = f"SELECT * FROM cities WHERE name = '{text}'"
        isCityExist = db_crud(self.connection, query_0, False)
        
        # Check if a row was returned
        if isCityExist is not None:
            # Get the last entry for the city and check if there is a value for each column and form the url_params again
            for row in isCityExist:
                city_id = row['id']
                query_weather = f"SELECT * FROM daily_weather_entries WHERE city_id = '{city_id}' ORDER BY ROWID DESC LIMIT 1"
                isWeatherEntryExist = db_crud(self.connection, query_weather, False)
                
                if isWeatherEntryExist is not None:
                    # Reset the 
                    url_params = ''
                    for columns in isWeatherEntryExist:
                        
                        if(minimum_temp and columns['min_temp'] is None):
                            url_params = url_params + "temperature_2m_min,"
                            
                        if(maximum_temp and columns['max_temp'] is None):
                            url_params = url_params + "temperature_2m_max,"
                            
                        if(mean_temp and columns['mean_temp'] is None):
                            url_params = url_params + "temperature_2m_mean,"
                        
                        if(precipitation_sum and columns['precipitation'] is None):
                            url_params = url_params + "precipitation_sum,"
                            
                        if(daylight_duration and columns['daylight_duration'] is None):
                            url_params = url_params + "daylight_duration,"
                            
                        if(uv_index_max and columns['uv_index_max'] is None):
                            url_params = url_params + "uv_index_max"
                            
                            
                    if(url_params):
                        daily_entry_result = make_request(f"https://archive-api.open-meteo.com/v1/archive?latitude={row['latitude']}&longitude={row['longitude']}&start_date=2000-01-01&end_date=2023-12-31&daily={url_params}&timezone=auto")
                
                        daily = daily_entry_result['daily']
                        get_values_to_update = url_params.split(',')
                        
                        for i, item in enumerate(daily['time']):
                            
                            columns = []
                            placeholders = ["?"]
                            values = []
                            
                            self.add_column('temperature_2m_min', columns, placeholders, values, 'min_temp', get_values_to_update, daily, '', i)
                            self.add_column('temperature_2m_max', columns, placeholders, values, 'max_temp', get_values_to_update, daily, '', i)
                            self.add_column('temperature_2m_mean', columns, placeholders, values, 'mean_temp', get_values_to_update, daily, '', i)
                            self.add_column('precipitation_sum', columns, placeholders, values, 'precipitation', get_values_to_update, daily, '', i)
                            self.add_column('daylight_duration', columns, placeholders, values, 'daylight_duration', get_values_to_update, daily, '', i)
                            self.add_column('uv_index_max', columns, placeholders, values, 'uv_index_max', get_values_to_update, daily, '', i)
                            
                            values.append(city_id)
                            values.append(daily['time'][i])

                            set_clause = ", ".join(f"{column} = ?" for column in columns) 
                            query = f"UPDATE daily_weather_entries SET {set_clause} WHERE city_id = ? AND date = ?"
                        
                            db_crud(self.connection, query, values, 'update')
                            
                        print(f"Successfully updated {len(daily['time'])} rows")

                else:
                    
                    daily_entry_result = make_request(f"https://archive-api.open-meteo.com/v1/archive?latitude={row['latitude']}&longitude={row['longitude']}&start_date=2000-01-01&end_date=2023-12-31&daily={url_params}&timezone=auto")
            
                    daily = daily_entry_result['daily']
                    get_values_to_update = url_params.split(',')
                    
                    for i, item in enumerate(daily['time']):
                
                        columns = ["date", "city_id"]
                        placeholders = ["?", "?"]
                        values = [daily['time'][i], city_id]
                        
                        self.add_column('temperature_2m_min', columns, placeholders, values, 'min_temp', get_values_to_update, daily, 'temperature_2m_min', i)
                        self.add_column('temperature_2m_max', columns, placeholders, values, 'max_temp', get_values_to_update, daily, 'temperature_2m_max', i)
                        self.add_column('temperature_2m_mean', columns, placeholders, values, 'mean_temp', get_values_to_update, daily, 'temperature_2m_mean', i)
                        self.add_column('precipitation_sum', columns, placeholders, values, 'precipitation', get_values_to_update, daily, 'precipitation_sum', i)
                        self.add_column('daylight_duration', columns, placeholders, values, 'daylight_duration', get_values_to_update, daily, 'daylight_duration', i)
                        self.add_column('uv_index_max', columns, placeholders, values, 'uv_index_max', get_values_to_update, daily, 'uv_index_max', i)
            
                        columns_str = f"({', '.join(columns)})"
                        placeholders_str = f"({', '.join(placeholders)})"
                        query = f"INSERT INTO daily_weather_entries {columns_str} VALUES {placeholders_str}"
                        
                        # tk_label(form, text="Loading...", x=300, y=420)
                        db_crud(self.connection, query, values, 'create')
                        
                    print(f"Successfully inserted {len(daily['time'])}")
        else:
            
            result = make_request(f"https://geocoding-api.open-meteo.com/v1/search?name={text}&count=1&language=en&format=json")
            result = result['results'][0]
            country = result['country']
            timezone = result['timezone']
            latitude = result['latitude']
            longitude = result['longitude']
            name = result['name']
            
            query = f"SELECT * FROM countries WHERE name = '{country}'"
            isCountryExist = db_crud(self.connection, query, False)
            
            if isCountryExist is None:
            
                query = "INSERT into countries (name, timezone) VALUES (?, ?)"
                values = (country, timezone)
                country_id = db_crud(self.connection, query, values, 'create')
            else:
                for country in isCountryExist:
                    
                    country_id = country['id']
            
            query_2 = "INSERT into cities (name, latitude, longitude, country_id) VALUES (?, ?, ?, ?)"
            values_2 = (name, latitude, longitude, country_id)
            city_id = db_crud(self.connection, query_2, values_2, 'create')
            
            daily_entry_result = make_request(f"https://archive-api.open-meteo.com/v1/archive?latitude={latitude}&longitude={longitude}&start_date=2000-01-01&end_date=2023-12-31&daily={url_params}&timezone=auto")
            
            daily = daily_entry_result['daily']
            
            for i, item in enumerate(daily['time']):
                
                columns = ["date", "city_id"]
                placeholders = ["?", "?"]
                values = [daily['time'][i], city_id]
                
                self.add_column(minimum_temp, columns, placeholders, values, 'min_temp', [], daily, 'temperature_2m_min', i, True)
                self.add_column(maximum_temp, columns, placeholders, values, 'max_temp', [], daily, 'temperature_2m_max', i, True)
                self.add_column(mean_temp, columns, placeholders, values, 'mean_temp', [], daily, 'temperature_2m_mean', i, True)
                self.add_column(precipitation_sum, columns, placeholders, values, 'precipitation', [], daily, 'precipitation_sum', i, True)
                self.add_column(daylight_duration, columns, placeholders, values, 'daylight_duration', [], daily, 'daylight_duration', i, True)
                self.add_column(uv_index_max, columns, placeholders, values, 'uv_index_max', [], daily, 'uv_index_max', i, True)
    
                columns_str = f"({', '.join(columns)})"
                placeholders_str = f"({', '.join(placeholders)})"
                query = f"INSERT INTO daily_weather_entries {columns_str} VALUES {placeholders_str}"
                
                tk_label(form, text="Loading...", x=300, y=420)
                db_crud(self.connection, query, values, 'create')
                
            print(f"Successfully inserted {len(daily['time'])}")
            # close_loader(form)
        

    def form4(self, form):
        tk_label(form, text="This tab shows Phase Four of the project.", x=400, y=0)
        
        y = 80
        tk_label(form, text='Enter a city to view the daily weather entries:', x=200, y=y)
        text_value = tk_input(form, text="Enter text", x=550, y=y)
        add_placeholder(text_value, "Enter text here")
        
        minimum_temp = tk.IntVar()
        minimum_temp.set(1)
        maximum_temp = tk.IntVar()
        maximum_temp.set(1)
        mean_temp = tk.IntVar()
        mean_temp.set(1)
        precipitation = tk.IntVar()
        precipitation.set(1)
        daylight_duration = tk.IntVar()
        uv_index_max = tk.IntVar()
        
        x = 350
        y = 170
        
        tk_label(form, text="Select an option to include any of the following in the data:", x=200, y=y-30)
        tk_checkbox(form, "Minimum Temperature", minimum_temp, x, y)
        tk_checkbox(form, "Maximum Temperature", maximum_temp, x, y+30)
        tk_checkbox(form, "Mean Temperature", mean_temp, x, y+60)
        tk_checkbox(form, "Precipitation", precipitation, x, y+90)
        tk_checkbox(form, "Daylight Duration", daylight_duration, x, y+120, False)
        tk_checkbox(form, "UV Index Maximum", uv_index_max, x, y+150, False)
        
        
        func = lambda: self.get_city_info(
            text_value.get(),
            minimum_temp.get(),
            maximum_temp.get(),
            mean_temp.get(),
            precipitation.get(),
            daylight_duration.get(),
            uv_index_max.get(),
            form
        )
        
        button = tk.Button(form, text= "Submit", command=func).place(x=400, y=y+250)