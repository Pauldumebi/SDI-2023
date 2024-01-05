
import sqlite3
from multiprocessing import connection

def get_cities(connection):
    
    with sqlite3.connect("db/CIS4044-N-SDI-OPENMETEO-PARTIAL.db") as connection:
        try:
            connection.row_factory = sqlite3.Row
            query = f"""
                SELECT id, name
                FROM cities
            """
            cursor = connection.cursor()
            results = cursor.execute(query)
            
            dict = {}
            
            for row in results:
                dict[row['name']] = row['id']
            
            return dict

        except sqlite3.OperationalError as ex:
            print(ex)
