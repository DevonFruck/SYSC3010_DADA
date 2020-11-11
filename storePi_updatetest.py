import http.client
import urllib.parse
import time
from datetime import date
from datetime import datetime
key = "K6Y0W11NP3QY2CJN"  # Put your API Key here

count = 1
temp = 2
humidity = 3
date = date.today().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M")

def storePiUpdate():
    while True: #Calculate CPU temperature of Raspberry Pi in Degrees C
        params = urllib.parse.urlencode({'field1': count, 'field2': temp,'field3': humidity,'field4': date, 'field5':time, 'key':key})
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

if __name__ == "__main__":
    while True:
        storePiUpdate()