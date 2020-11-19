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
key = "K6Y0W11NP3QY2CJN"  # Put your API Key here

count = 20
temp = 77
humidity = 66


def storePiUpdate():
    while True: #Calculate CPU temperature of Raspberry Pi in Degrees C
        params = urllib.parse.urlencode({'field1': count, 'field2': temp,'field3': humidity, 'key':key})
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
    
def retriveOtherStoreCount():
    store2 = requests.get(s2URL).json()
    Count2 = store2['feeds'][0]['field1']
    return int(Count2)

if __name__ == "__main__":
    while True:
        storePiUpdate()