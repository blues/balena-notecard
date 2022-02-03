import os
import json
import notecard
import notecard_pseudo_sensor
from periphery import I2C
import time


productUID = "com.blues.tvantoll:weather" #os.environ['productUID']
noteFile = "sensors.qo" #os.environ['noteFile']
card = 0

print(productUID)
print(noteFile)


def sendMessage(message):
  global noteFile
  global card

  req = {"req": "note.add"}
  req["file"] = noteFile
  req["sync"] = True
  req["body"] = message

  rsp = card.Transaction(req)
  print(rsp)

 

def main():
  global productUID
  global card

  print("Initializing blues...")

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
    msg = { "temp": temp }
    print(temp)
    sendMessage(msg)
    time.sleep(15)


if __name__ == "__main__":
    main()