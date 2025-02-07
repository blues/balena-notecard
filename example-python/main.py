import random
import requests
import time

req = {"req": "hub.set"}
req["product"] = "com.blues.tvantoll:weather"
req["mode"] = "continuous"

url = "http://notecard:3434"
headers = {"Content-Type": "application/json"}
result = requests.post(url, json=req, headers=headers)
print(result.text)

while True:
  temp = round(random.uniform(20, 25), 4)
  humidity = round(random.uniform(45, 50), 4)
  req = {"req": "note.add"}
  req["file"] = "sensors.qo"
  req["sync"] = True
  req["body"] = {"temp": temp, "humidity": humidity}

  result = requests.post(url, json=req, headers=headers)
  print(result.text)
 
  time.sleep(15)