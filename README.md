# Notecard Balena Block

This is a balena [Block](https://www.balena.io/blog/balenablocks-public-roadmap/) for interfacing with the [Blues Wireless Notecard](https://blues.io/products/notecard/).

Add this block to your Balena fleet to easily send data to your cloud backend via a low-power cellular connection.

## Prerequisites

To add the Blues Block to your fleet you need to add Blues Wireless connectivity to all of your devices. To you will need to:

* Purchase a [Notecard Raspberry Pi Kit](https://shop.blues.io/products/raspberry-pi-starter-kit). 
* Create a [Notehub](https://notehub.io/) account.

And if all of this is new to you, we’d recommend going through the [Notecard quickstart tutorial](https://dev.blues.io/quickstart/notecard-quickstart) before continuing.

## Block configuration

To add the Blues Block, add this service in your `docker-compose.yml`, as shown below. 

```
  notecard:
    image: "bh.cr/blues_wireless/notecard-<architecture>"
    devices:
      - "/dev/i2c-1:/dev/i2c-1"
    expose:
      - "8080"
    privileged: true
```

Use `aarch64` on the architecture if you are using a Raspberry Pi 4.


## Usage

Once you have everything deployed on your fleet, you can use the Notecard by POSTing JSON requests to `http://notecard:8080`. 

![diagram-blues-balena](https://user-images.githubusercontent.com/173156/158283207-0568c9eb-9e3a-451d-b426-27c75b983e85.png)

For example, the following code performs a [`hub.set` command](https://dev.blues.io/reference/notecard-api/hub-requests/#hub-set) on the Notecard.

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
