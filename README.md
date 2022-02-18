# Notecard Balena Block

A [balenaBlock](https://github.com/balenablocks) for interfacing with the [Blues Wireless Notecard](https://blues.io/products/notecard/).

Add this block to your Balena application to easily send data to your cloud backend via a cellular connection.

## Installation

???

## Usage

Once installed, you can use the Notecard by POSTing JSON requests to `http://notecard:8080`. For example, the following code performs a [`hub.set` command](https://dev.blues.io/reference/notecard-api/hub-requests/#hub-set) on the Notecard.

```python
import requests

req = {"req": "hub.set"}
req["product"] = "com.company.name:myproject"
req["mode"] = "continuous"

url = "http://notecard:8080"
headers = {"Content-Type": "application/json"}
result = requests.post(url, json=req, headers=headers)
```

> **NOTE**: See the [`example-python` folder](example) for a full sample script.

Refer to the [Notecard quickstart](https://dev.blues.io/quickstart/notecard-quickstart/notecarrier-pi/) for more information on how to set up and use a Blues Wireless Notecard.
