#To create environment  
# Run> python -m venv myenv
# To activate the virtual environment
# Run> myenv\Scripts\activate
#To install the package
# pip install matplotlib.pyplot

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
connection = sqlite3.connect("../db/CIS4044-N-SDI-OPENMETEO-PARTIAL.db")

# For city 'Middlesbrough'
city_name = 'Middlesbrough'

# Query to select 7 days of precipitation data for the specified city
query = f"""
    SELECT date, precipitation
    FROM daily_weather_entries
    WHERE city_id = (SELECT id FROM cities WHERE name = 'Middlesbrough')
    ORDER BY date
    LIMIT 7
"""

# Read data from the database into a DataFrame
precipitation_data = pd.read_sql_query(query, connection, params=(city_name,))

# Close the database connection
connection.close()

# Plotting the bar chart
plt.bar(precipitation_data['date'], precipitation_data['precipitation'])
plt.title(f'7-Day Precipitation for {city_name}')
plt.xlabel('Date')
plt.ylabel('Precipitation')
plt.show()
