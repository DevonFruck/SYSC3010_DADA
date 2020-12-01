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
    
    #request data and convert it to a json string - Done at nearly same time to avoid mismatched time stamps. Everything after this is done procedurally 
    store1 = requests.get(s1URL).json()
    store2 = requests.get(s2URL).json()
    
    #Begin Store 1 Process
    
    #find values required for database from json string
    Count1 = int(store1['feeds'][0]['field1'])
    Temp1 = float(store1['feeds'][0]['field2'])
    Hum1 = float(store1['feeds'][0]['field3'])
    
    #confirm values fall into expected range, and are not extranneous 
    if Count1 < 0:
        Count1 = 0
    if Temp1 < -15 or Temp1 > 60:
        print("Invalid temperature")
        return False
    if Hum1 < 0 or Hum1 > 100:
        print("Invalid humidity")
        return False
        
    #Find values of recorded date and time 
    Date1 = store1['feeds'][0]['created_at']
    Date1 = Date1[0:10]
    #print(Date1)
    Time1 = store1['feeds'][0]['created_at']
    Time1 = Time1[11:16]
    print(Time1)
    
    #Insert recorded values into database
    cursor.execute('''INSERT INTO Store2Data (date,time,count,temperature,humidity) VALUES (?,?,?,?,?)''',(Date1, Time1, Count1, Temp1, Hum1))
    conn.commit()
    #For demo only
    print("Values stored")
    
    #FOR DEMOS ONLY WILL BE COMMENTED OUT LATER - Print selected rows' data
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
    Count2 = int(store2['feeds'][0]['field1'])
    Temp2 = float(store2['feeds'][0]['field2'])
    Hum2 = float(store2['feeds'][0]['field3'])
    
    #confirm values fall into expected range, and are not extranneous.
    #If count is negative, record it as 0 - means more people left than entered, 
    #   maybe an employee entering through a back door
    #If environment values are extranneous, exit funciton with failed status.
    if Count2 < 0:
        Count2 = 0
    if Temp2 < -15 or Temp1 > 60:
        print("Invalid temperature")
        return False
    if Hum2 < 0 or Hum1 > 100:
        print("Invalid humidity")
        return False
    
    #Insert recorded values into database
    #Uses Date1 and Time1 to avoid query errors that come up when timestamps do not match exactly. Pull is done at nearly the same time, so this is fine.
    cursor.execute('''INSERT INTO Store2Data (date,time,count,temperature,humidity) VALUES (?,?,?,?,?)''',(Date1, Time1, Count2, Temp2, Hum2))
    conn.commit()
    #For demos only
    print("Values stored")
    
    
    #Printing values are only for Demo purposes only 
    cursor.execute('''SELECT * FROM Store2Data''')
    for row in cursor:
        print(row['count'],row['temperature'],row['humidity'],row['date'],row['time'])
#     print(Count2)
#     print(Temp2)
#     print(Hum2)
    
    conn.close()
    return True
    
if __name__ == '__main__':
    
    #Every 5 mins(300 seconds) update the database with the recorded values.
    while(True):
        #If the storage to the database worked, wait 5 minutes and then store next data point
        if retrieveDataFromTS():
            #Using 15 Seconds for demos
            time.sleep(15)
        #If the storage to the database failed, try again for clean values.
        else:
            retrieveDataFromTS()


