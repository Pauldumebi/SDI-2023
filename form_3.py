from helpers.widgets import tk_options, tk_label
import tkinter as tk
from helpers.utils import get_place, destroy_window, db_crud, database_connection
from tkinter import messagebox

class PhaseThreeForm:
    def __init__(self):
        self.connection =  database_connection()
        
    def delete_place(self, cities, selected_city, dropdown_var, dropdown_menu, table='cities'):
        
        confirmed = messagebox.askyesno("Confirmation", f"Are you sure you want to delete {selected_city} {'deleting this city will remove all associated daily weather entries' if table == 'cities' else ''}")
        
        if not confirmed:
            return  # Do nothing if the user clicks 'No'
        
        delete_values = str(cities[selected_city])
        
        if table == 'countries':
            
            query = f"SELECT * FROM cities WHERE country_id = {delete_values}"
            get_city_id = db_crud(self.connection, query, False)
            
            if get_city_id  is not None:
                for row in get_city_id:
                    print(row['id'], 'id')
                    delete_values_city = row['id']
                    
                delete_query = f"DELETE FROM cities WHERE country_id = ?"
                deleted = db_crud(self.connection, delete_query, (str(delete_values_city), ), 'delete')
                
            delete_values_2 = (str(delete_values_city), )  
        else:
            delete_values_2 = (delete_values, )
            
        delete_query = f"DELETE FROM daily_weather_entries WHERE city_id = ?"        
        deleted = db_crud(self.connection, delete_query, delete_values_2, 'delete')
        
        # Delete final value
        delete_query_2 = f"DELETE FROM {table} WHERE id = ?"
        print(f'{deleted} row(s) were deleted from {table}')
        
        deleted_2 = db_crud(self.connection, delete_query_2, (delete_values, ), 'delete')
        print(f"{deleted_2} row(s) were deleted from {table}")
        
        messagebox.showinfo('showinfo', 'You need to restart the application for changes to take place ')
    
    def form3(self, form):
        tk_label(form, text="This tab shows Phase Three of the project. Click any of the buttons below to get started 🥺", x=100, y=20)
        
        if(self.connection is not None):
            destroy_window(form)
            
            y = 70
                    
            cities = get_place(self.connection)
            selected_value = tk.StringVar(form)
            default_city = list(cities)[0] if cities else ''
            selected_value.set(default_city)
            
            options = cities.keys() if cities else []
            tk_label(form, text="Select a City: ", x=150, y=y)
            dropdown_menu = tk.OptionMenu(form, selected_value, *options)
            dropdown_menu.place(x=250, y=y)
            
            func = lambda: self.delete_place (
                cities,
                selected_value.get(),
                selected_value,
                dropdown_menu
            )
 