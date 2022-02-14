from flask import Flask, request
from flask_cors import CORS
import threading
import json
import notecard
from periphery import I2C

PRODUCT_UID = "com.blues.tvantoll:weather" #os.environ['productUID']
NOTE_FILE = "sensors.qo" #os.environ['noteFile']
NOTE_MODE = "continuous" #os.environ["noteMode"]

app = Flask(__name__)

CORS(app, resources={ r'/*': {'origins': '*'}}, supports_credentials=True)

print("Initializing Notecard...")

port = I2C("/dev/i2c-1")
card = notecard.OpenI2C(port, 0, 0)

req = {"req": "hub.set"}
req["product"] = PRODUCT_UID
req["mode"] = NOTE_MODE

print(json.dumps(req))

rsp = card.Transaction(req)
print(rsp)

@app.route('/', methods=['POST'])
def send():
  try:
    sendMessage(request.json)
  except:
    return "Failed to send the data"

  return "The data was successfully sent"

def sendMessage(message):
  req = {"req": "note.add"}
  req["file"] = NOTE_FILE
  req["body"] = message

  rsp = card.Transaction(req)
  print(rsp)

def main():
  global productUID
  global card

if __name__ == "__main__":
  t = threading.Thread(target=main, args=())
  t.daemon = True
  t.start()

  print("Starting blues notecard thread...")
  threading.Thread(target=main,daemon=True).start()

  app.run(host='0.0.0.0', port='8080', debug=False)