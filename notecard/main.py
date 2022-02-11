import socket

from flask import Flask, render_template, Response, request, jsonify
from flask_cors import CORS,cross_origin
import threading

import json
import notecard
import notecard_pseudo_sensor
from periphery import I2C
import time

# async_mode = None
# runner = None

# NOTE_FILE = os.environ['noteFile']
# PRODUCT_UID = os.environ['productUID']

productUID = "com.blues.tvantoll:weather" #os.environ['productUID']
noteFile = "sensors.qo" #os.environ['noteFile']
# card = 0

# print(productUID)
# print(noteFile)

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'

CORS(app, resources={ r'/*': {'origins': '*'}}, supports_credentials=True)

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

# @app.route("/")
# def hello_world():
#   print("made it!!!!!!!!!!!")
#   return "<p>Hello, World!</p>"

@app.route('/send', methods=['POST'])
def send():
  print("POST!!!!")
  sendMessage("whatever")

  return "<p>Hello post</p>"

def sendMessage(message):
  # global noteFile
  # global card

  req = {"req": "note.add"}
  req["file"] = noteFile
  req["sync"] = True
  req["body"] = { "hello": "world" }

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
    #socketio.run(app,host='0.0.0.0', port='8080', debug=False)

    #main()