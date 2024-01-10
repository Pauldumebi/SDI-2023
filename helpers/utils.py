
import sqlite3
from multiprocessing import connection
from  datetime import datetime
from tkinter import messagebox
import os
import requests


def make_request(url):
    req = requests.get(url)
    response = req.json()
    
    if req.status_code == 200:
        return response
    
def get_place(connection, table='cities'):
    
    try:
        connection.row_factory = sqlite3.Row
        query = f"""
            SELECT id, name
            FROM {table}
        """
        cursor = connection.cursor()
        results = cursor.execute(query)
        
        dict = {}
        
        for row in results:
            dict[row['name']] = row['id']
        
      