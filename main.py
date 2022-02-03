import json
import notecard
import notecard_pseudo_sensor
from periphery import I2C
import time

productUID = "com.blues.tvantoll:weather"

port = I2C("/dev/i2c-1")
card = notecard.OpenI2C(port, 0, 0)
sensor = notecard_pseudo_sensor.NotecardPseudoSensor(card)

req = {"req": "hub.set"}
req["product"] = productUID
req["mode"] = "continuous"
 
print(json.dumps(req))
 
rsp = card.Transaction(req)
print(rsp)

while True:
  temp = sensor.temp()
  print(temp)

  req = {"req": "note.add"}
  req["file"] = "sensors.qo"
  req["sync"] = True
  req["body"] = { "temp": temp }
  rsp = card.Transaction(req)
  print(rsp)
 
  time.sleep(15)
