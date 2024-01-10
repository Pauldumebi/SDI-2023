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
            get_city_id = db_crud(self.connection, query)
            
            for row in get_city_id:
                print(row['id'], 'id')
                delete_values_city = row['id']
                
            delete_query = f"DELETE FROM cities WHERE country_id = ?"
            deleted = db_crud(self.connection, delete_query, delete_values_city, 'delete')
            delete_values_2 = str(delete_values_city)
            
            print(deleted, f"{deleted} rows were deleted")
            
        else:
            delete_values_2 = delete_values
            
        delete_query = f"DELETE FROM daily_weather_entries WHERE city_id = ?"
        
        print(delete_query)
        print(delete_values_2, 'delete_values')
        
        deleted = db_crud(self.connection, delete_query, delete_values_2, 'delete')
        print(deleted, f"{deleted} rows were deleted")
            
        # Delete final value
        delete_query_2 = f"DELETE FROM {table} WHERE id = ?"
        print(delete_values, 'delete_values')
        
        deleted_2 = db_crud(self.connection, delete_query_2, delete_values, 'delete')
        print(deleted_2, f"{deleted_2} rows were deleted")
        
        # updated_values = get_place(self.connection)
        # print(updated_values, 'updated_values')

        # # Update the dropdown with the updated values
        # dropdown_var.set("")  # Clear the current selection
        # dropdown_menu['menu'].delete(0, 'end')  # Clear the current menu items

        # for value in updated_values:
        #     print(value, 'value')
        #     dropdown_menu['menu'].add_command(label=value, command=lambda v=value: dropdown_var.set(v))

        # get_place(connection)
        
        # tk_options(form, selected_value, cities.keys(), x=250, y=y)
    
    def form3(self, form):
        tk_label(form, text="This tab shows Phase Three of the project. Click any of the buttons below to get started", x=100, y=20)
        
        if(self.connection is not None):
            destroy_window(form)
            
            y = 70
                    
            cities = get_place(self.connection)
            selected_value = tk.StringVar(form)
            default_city = list(cities)[0] if cities else ''
            selected_value.set(default_city)
            
            options = cities.keys() if cities else []
            tk_label(form, text="Select a City: ", x=150, y=y)
            dropdown_menu = tk_options(form, selected_value, options, x=250, y=y)
            
            func = lambda: self.delete_place (
                cities,
                selected_value.get(),
                selected_value,
                dropdown_menu
            )
            
            tk.Button(form, text= "Delete", command=func).place(x=400, y=y-4)
            
            y = 150
            
            countries = get_place(self.connection, 'countries')
            selected_value_2 = tk.StringVar(form)
            selected_value_2.set(list(countries)[0])
            
            tk_label(form, text="Select a Country: ", x=150, y=y)
            dropdown_menu = tk_options(form, selected_value_2, countries.keys(), x=280, y=y)
            
            func = lambda: self.delete_place (
                countries,
                selected_value_2.get(),
                selected_value,
                dropdown_menu,
                'countries'
            )
            
            tk.Button(form, text= "Delete", command=func).place(x=420, y=y-4)
    