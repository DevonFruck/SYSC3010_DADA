from urllib.request import * 
from urllib.parse import *
from pip._vendor import requests
import json
import sqlite3

#ThingSpeak API key for each channel.
def retrieveDataFromTS()

    #URL template for pulling data from ThingSpeak
    URL1 = "https://api.thingspeak.com/channels/1149760/fields/1.json?api_key="
    URL2 = "https://api.thingspeak.com/channels/1149760/fields/2.json?results=2"
    URL3 = "https://api.thingspeak.com/channels/1149760/fields/3.json?results=2"


    store1Count = requests.get(URL1).json()
    store1Temp = requests.get(URL2).json()
    store1Hum = requests.getURL(URL3).json()
    
    
    Count1 = store1Count[][]
    


