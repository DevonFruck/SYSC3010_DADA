#Code taken from website 'https://iotdesignpro.com/projects/how-to-send-data-to-thingspeak-cloud-using-raspberry-pi'
import http.client
import urllib.parse
import time
from datetime import date
from datetime import datetime
key = "CDSY7SI5HEFWKVCS"  # Put your API Key here


#d1 = date.today().strftime("%d/%m/%Y")
#time1 = datetime.now().strftime("%H:%M")

def storePiUpdate():
    count = 23
    temp = 67
    humidity = 958
    while True: #Uploading store data to thingspeak
        params = urllib.parse.urlencode({'field1': count, 'field2': temp, 'field3': humidity, 'key':key})
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
