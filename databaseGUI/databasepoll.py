#This is Python3 code

import sqlite3

def database_retrieve():
    #connect to database file
    dbconnect = sqlite3.connect("database.db")

    #set row factory to sqlite3.row class to access columns
    dbconnect.row_factory = sqlite3.Row

    #creating cursor to work with db
    cursor = dbconnect.cursor()

    #fetch the most recent record in database (at the bottom of table)
    cursor.execute("SELECT * FROM store1 ORDER BY rowid DESC LIMIT 1")

    for row in cursor:
        store1_data = [row['count'], row['temperature'], row['humidity']]

    cursor.execute("SELECT MAX(count) FROM store1 DESC LIMIT 1")
    store1_data.append(cursor.fetchone()[0])

    ##Fetching from store2 table
    cursor.execute("SELECT * FROM store2 ORDER BY rowid DESC LIMIT 1")

    for row in cursor:
        store2_data = [row['count'], row['temperature'], row['humidity']]

    cursor.execute("SELECT MAX(count) FROM store2 DESC LIMIT 1")
    store2_data.append(cursor.fetchone()[0])
    
    #close connection
    dbconnect.close()
    
    return store1_data, store2_data
