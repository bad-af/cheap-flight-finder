import sqlite3
def initialize_database():
    connection = sqlite3.connect("flights.db")
    query = ("CREATE TABLE IF NOT EXISTS flight_prices (id INTEGER PRIMARY KEY,"
             "origin TEXT NOT NULL,"
             "destination TEXT NOT NULL)")
    connection.execute(query)
    connection.close()

def check_tables():
    connection = sqlite3.connect("flights.db")
    query = ("SELECT name FROM sqlite_master WHERE type='table' AND name='flight_prices'")
    cursor = connection.execute(query)
    result = cursor.fetchall()
    print(result)
    connection.close()
check_tables()

