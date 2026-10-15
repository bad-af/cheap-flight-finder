import sqlite3
def initialize_database():
    connection = sqlite3.connect("flights.db")
    query = ("CREATE TABLE IF NOT EXISTS flight_prices (id INTEGER PRIMARY KEY,"
            "origin TEXT NOT NULL,"
            "destination TEXT NOT NULL)")
    connection.execute(query)
    connection.close()
initialize_database()

def check_tables():
    connection = sqlite3.connect("flights.db")
    query = ("SELECT name FROM sqlite_master WHERE type='table' AND name='flight_prices'")
    cursor = connection.execute(query)
    result = cursor.fetchall()
    print(result)
    connection.close()
check_tables()

def columns_exist(column_name):
    connection = sqlite3.connect("flights.db")
    query = "PRAGMA table_info(flight_prices)"
    cursor = connection.execute(query)
    result = cursor.fetchall()

    exists = False

    for column in result:
        if column_name == column[1]:
            exists = True
            break

    connection.close()
    return exists

def add_departure_date_column():
    connection = sqlite3.connect("flights.db")
    if not columns_exist("departure_date"):
        query = ("ALTER TABLE flight_prices "
                "ADD COLUMN departure_date TEXT")
        connection.execute(query)
    connection.close()
add_departure_date_column()

def add_return_date_column():
    connection = sqlite3.connect("flights.db")
    if not columns_exist("return_date"):
        query = ("ALTER TABLE flight_prices "
                "ADD COLUMN return_date TEXT")
        connection.execute(query)
    connection.close()
add_return_date_column()

def add_price_column() :
    connection = sqlite3.connect("flights.db")
    if not columns_exist("price"):
        query = ("ALTER TABLE flight_prices "
                "ADD COLUMN price REAL")
        connection.execute(query)
    connection.close()
add_price_column()

def add_currency_column():
    connection = sqlite3.connect("flights.db")
    if not columns_exist("currency"):
        query = ("ALTER TABLE flight_prices "
                "ADD COLUMN currency TEXT")
        connection.execute(query)
    connection.close()
add_currency_column()

def add_source_column():
    connection = sqlite3.connect("flights.db")
    if not columns_exist("source"):
        query = ("ALTER TABLE flight_prices "
                "ADD COLUMN source TEXT")
        connection.execute(query)
    connection.close()
add_source_column()

def add_searched_at_column():
    connection = sqlite3.connect("flights.db")
    if not columns_exist("searched_at"):
        query = ("ALTER TABLE flight_prices "
                "ADD COLUMN searched_at TEXT")
        connection.execute(query)
    connection.close()
add_searched_at_column()

def check_columns():
    connection = sqlite3.connect("flights.db")
    query = "PRAGMA table_info(flight_prices)"
    cursor = connection.execute(query)
    result = cursor.fetchall()

    for column in result:
        print(column[1])

    connection.close()

check_columns()








