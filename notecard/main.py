from flask import Flask, request
from flask_cors import CORS
import notecard
from periphery import I2C

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

print("Initializing Notecard...")

port = I2C("/dev/i2c-1")
card = notecard.OpenI2C(port, 0, 0)

@app.route("/", methods=["POST"])
def send():
  try:
    sendRequest(request.json)
  except:
    return "Failed to send data to Notehub"

  return "Successfully sent data to Notehub"

def sendRequest(requestJSON):
  try:
    print('the json to send to the Notecard')
    print(requestJSON)
    rsp = card.Transaction(requestJSON)
    print(rsp)
  except Exception as e:
    print(e)
    print("Failed to send data to Notehub")

if __name__ == "__main__":
  print("Starting blues notecard thread...")
  app.run(host='0.0.0.0', port='8080', debug=False)