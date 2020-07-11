# imports
import pyodbc
import pandas as pd

def get_data():
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-INR29OP;'
                        'Database=healthdata;'
                        'Trusted_Connection=yes;')

    ## used to exec SQL queries
    cursor = conn.cursor()

    data = pd.read_sql_query('select * from data_clean', conn)
    return data
