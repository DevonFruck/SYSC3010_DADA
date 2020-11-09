#Imports and dependencies
from urllib.request import * 
from urllib.parse import *
from pip._vendor import requests
import json
import sqlite3


def retrieveDataFromTS():
    #setup

    #Database connection
    conn = sqlite3.connect("mainDatabase.db")

    #set up access point 
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    #URLs for pulling data from ThingSpeak
    s1URL = "https://api.thingspeak.com/channels/1149760/feeds.json?results=3"
    s2URL = ""
    
    #request data and convert it to a json string
    store1 = requests.get(s1URL).json()
    store2 = requests.get(s2URL).json()
    
    #Begin Store 1 Process
    
    #find values required for database from json string
    for (i) in range(3):
        if (store1['feeds'][i]['field1'] != None):
            Count1 = store1['feeds'][i]['field1']
        else if (store1['feeds'][i]['field2'] != None)
            Hum1 = store1['feeds'][i]['field2']
        else 
            Temp1 = store1['feeds'][i]['field3']

    #Find values of recorded date and time 
    Date1 = store1['feeds']['created_at']
    Date1 = Date1[0:10]
    Time1 = store1['feeds']['created_at']
    Time1 = Time1[12:16]
    
    #Insert recorded values into database
    cursor.execute('''insert into store1Data values (?,?,?,?,?)''',(Date1, Time1, Count1, Temp1, Hum1))

    #Begin Store 2 Process.
    
    #find values required for database from json string
    for (i) in range(3):
        if (store2['feeds'][i]['field1'] != None):
            Count2 = store2['feeds'][i]['field1']
        else if (store2['feeds'][i]['field2'] != None)
            Hum2 = store2['feeds'][i]['field2']
        else 
            Temp2 = store2['feeds'][i]['field3']
    
    #Find values of recorded date and time 
    Date2 = store2['feeds']['created_at']
    Date2 = Date2[0:10]
    Time2 = store2['feeds']['created_at']
    Time2 = Time2[12:16]
    
    #Insert recorded values into database
    cursor.execute('''insert into store2Data values (?,?,?,?,?)''',(Date1, Time1, Count2, Temp2, Hum2))
    
    
    
if __name__ == '__main__':
    
    #Every 5 mins(300 seconds) update the database with the recorded values.
    while(True):
        retrieveDataFromTS()
        sleep(300)


