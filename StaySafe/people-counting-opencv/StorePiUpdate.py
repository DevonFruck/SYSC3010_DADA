#Code taken from website 'https://iotdesignpro.com/projects/how-to-send-data-to-thingspeak-cloud-using-raspberry-pi'
import http.client
import urllib.parse
from urllib.request import *
from urllib.parse import *
from pip._vendor import requests
import json
import time
from datetime import date
from datetime import datetime

s1key = "CDSY7SI5HEFWKVCS"  #API Key for store 1
s2key = "K6Y0W11NP3QY2CJN" #API key for store 2
s1URL = "https://api.thingspeak.com/channels/1225774/feeds.json?api_key=QO9WBN28PA1X46X8&results=1&timezone=America/New_York"
s2URL = "https://api.thingspeak.com/channels/1225784/feeds.json?api_key=6UIX8KY589EGWK9J&results=1&timezone=America/New_York"
storeList = [s1URL, s2URL]


def storePiUpdate(count, temp, humidity, storeID):
    writeKey = ""
    if int(storeID) == 1:
        writeKey = str(s1key)
    if int(storeID) == 2:
        writeKey = str(s2key)
    
    while True: #Uploading store data to thingspeak
        params = urllib.parse.urlencode({'field1': count, 'field2': temp, 'field3': humidity, 'key': writeKey})
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print(count)
            print(temp)
            print(humidity)
            print(response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print("connection failed")
        break

def retrieveOtherStoreCount(count):
    leastStoreCount = count
    storeNum = 1
    for i in range(len(storeList)):
        storeCurrent = requests.get(storeList[i]).json()
        if int(storeCurrent['feeds'][0]['field1']) < leastStoreCount:
            leastStoreCount = int(storeCurrent['feeds'][0]['field1'])
            storeNum = i 
    return storeNum+1

if __name__ == "__main__":
    while True:
        storePiUpdate()
