import sqlite3

# Long = 54.57623
# Lat = -1.23483
# Name = Middlesbrough
# country_id = 1


# Long = 51.50853
# Lat = -0.12574
# Name = London
# country_id = 1


# Long = 48.85341
# Lat = 2.3488
# Name = Paris
# country_id = 2

# Long = 43.60426
# Lat = 1.44367
# Name = Toulouse
# country_id = 2
            
with sqlite3.connect("db/CIS4044-N-SDI-OPENMETEO-PARTIAL.db") as connection:

    def perform_delete(connection, query, values):
        try:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute(query, values)
            connection.commit()
                    
        except sqlite3.OperationalError as ex:
            print(ex)
                
                
    # query = "INSERT INTO cities (name, longitude, latitude, country_id) VALUES (?, ?, ?, ?)"
    # values = ["Middlesbrough", "54.57623", "-1.23483", "1"]
    
    # query = "INSERT INTO cities (name, 