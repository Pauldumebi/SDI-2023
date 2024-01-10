import sqlite3
import matplotlib.pyplot as plt
from datetime import timedelta, datetime


def plot_average_temperature_cities(connection, start_date, end_date):
    try:
        connection.row_factory = sqlite3.Row
        # Define the query to get average temperatures for each city within the specified date range
        query = """
        SELECT AVG(mean_temp) as avg_temperature, cities.name as city_name 
        FROM daily_weather_entries
        JOIN cities ON daily_weather_entries.city_id = cities.id
        WHERE date BETWEEN ? AND ?
        GROUP BY cities.name
        """
        
        # Get a cursor object from the database connection
        cursor = connection.cursor()

        # Execute the query via the cursor object, using placeholders
        results = cursor.execute(query, (start_date, end_date))

        # Fetch all rows from the results
        rows = results.fetchall()

        if rows:
            # Extract city names and average temperatures from the results
            city_names = [row['city_name'] for row i