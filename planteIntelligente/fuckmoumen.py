import requests
import serial
import time
import simplejson as json

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

data = " "
url = "https://192.168.1.13:45455/api/PlanStateValues"
headers = {'content-type': 'application/json'}
while True :
        try :
                ser = serial.Serial('/dev/ttyACM0',9600)
                line = ser.readline().decode("utf-8")
                data=json.loads(line)
                print(line)
        except :
                print("Loading")
        if data != " " :
                try :
                        r = requests.post(url = url, data=json.dumps(data),
                        headers = headers,  verify = False)
                        data = " "
                        time.sleep(1)
                except json.decoder.JSONDecodeError :
                        print(Loading)
                except KeyError :
                        print(Loading)
                except TypeError :
                        print(Loading)
# BY AKRAM + MOTASSIM