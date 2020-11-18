#Imports and dependencies
from urllib.request import * 
from urllib.parse import *
from pip._vendor import requests
import json
import sqlite3
import time


def retrieveDataFromTS():
    #setup

    #Database connection
    conn = sqlite3.connect("mainDatabase.db")

    #set up access point 
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    #URLs for pulling data from ThingSpeak
    s1URL = "https://api.thingspeak.com/channels/1225774/feeds.json?api_key=QO9WBN28PA1X46X8&results=1&timezone=America/New_York"
    s2URL = "https://api.thingspeak.com/channels/1225784/feeds.json?api_key=6UIX8KY589EGWK9J&results=1&timezone=America/New_York"
    
    #request data and convert it to a json string
    store1 = requests.get(s1URL).json()
    store2 = requests.get(s2URL).json()
    
    #Begin Store 1 Process
    
    #find values required for database from json string
    Count1 = store1['feeds'][0]['field1']
    Temp1 = store1['feeds'][0]['field2']
    Hum1 = store1['feeds'][0]['field3']

    #Find values of recorded date and time 
    Date1 = store1['feeds'][0]['created_at']
    Date1 = Date1[0:10]
    #print(Date1)
    Time1 = store1['feeds'][0]['created_at']
    Time1 = Time1[12:16]
    #print(Time1)
    
    #Insert recorded values into database
    cursor.execute('''INSERT INTO Store2Data (date,time,count,temperature,humidity) VALUES (?,?,?,?,?)''',(Date1, Time1, Count1, Temp1, Hum1))
    conn.commit()
    print("Values stored")
    
    #FOR DEMO ONLY - Print selected rows' data
    cursor.execute('''SELECT * FROM Store1Data''')
    for row in cursor:
        print(row['count'],row['temperature'],row['humidity'],row['date'],row['time'])
    
#     print(Count1)
#     print(Temp1)
#     print(Hum1)
#     print(Date1)
#     print(Time1)
    
    #Begin Store 2 Process.
    
    #find values required for database from json string
    Count2 = store2['feeds'][0]['field1']
    Temp2 = store2['feeds'][0]['field2']
    Hum2 = store2['feeds'][0]['field3']
    
    #Insert recorded values into database
    #Uses Date1 and Time1 to avoid query errors that come up when timestamps do not match exactly. Pull is done at nearly the same time, so this is fine.
    cursor.execute('''INSERT INTO Store2Data (date,time,count,temperature,humidity) VALUES (?,?,?,?,?)''',(Date1, Time1, Count2, Temp2, Hum2))
    conn.commit()
    print("Values stored")
    
    cursor.execute('''SELECT * FROM Store2Data''')
    for row in cursor:
        print(row['count'],row['temperature'],row['humidity'],row['date'],row['time'])
#     print(Count2)
#     print(Temp2)
#     print(Hum2)
    
    conn.close()
    
if __name__ == '__main__':
    
    #Every 5 mins(300 seconds) update the database with the recorded values.
    while(True):
        retrieveDataFromTS()
        time.sleep(30)


