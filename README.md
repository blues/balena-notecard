# Notecard Balena Block

A [balenaBlock](https://github.com/balenablocks) for interfacing with the [Blues Wireless Notecard](https://blues.io/products/notecard/).

Add this block to your Balena application to easily send data to cloud backends via a cellular connection.

## Prerequisites

This integration assumes that you have done the following.

1) Purchased a Notecard. If you have not, you can find Notecard developments kits on [shop.blues.io](https://shop.blues.io).
2) Set up a Notehub account. If you have not, you can create one at [notehub.io](notehub.io).

And if all of this is new to you, we’d recommend going through the [Notecard quickstart tutorial](https://dev.blues.io/quickstart/notecard-quickstart) before continuing.

## Docker Setup

To use this project, create a container in your `docker-compose.yml` file as shown below.

```
version: "2.1"
services:
  notecard:
    image: "tjvantoll/balena-notecard"
    build: ./src
    devices:
      - "/dev/i2c-1:/dev/i2c-1"
    expose:
      - "8080"
    privileged: true
```

## Usage

Once you have everything installed, you can use the Notecard by POSTing JSON requests to `http://notecard:8080`. For example, the following code performs a [`hub.set` command](https://dev.blues.io/reference/notecard-api/hub-requests/#hub-set) on the Notecard.

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
