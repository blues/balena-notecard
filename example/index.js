const axios = require("axios");

async function makeRequest(json) {
  try {
    await axios.post("http://notecard:8080", JSON.stringify(json), {
      headers: {
        "Content-Type": "application/json",
      },
    });
    console.log("Successful request");
  } catch (e) {
    console.log("Request did not work when trying to send", json);
    console.log("Error", e.message);
  }
}

async function main() {
  console.log("starting");

  console.log("sending first request");
  makeRequest({
    req: "hub.set",
    product: "com.blues.tvantoll:weather",
  });

  setTimeout(() => {
    console.log("sending second request");
    makeRequest({
      req: "note.add",
      body: {
        temp: 888,
        humid: 999,
      },
    });

    makeRequest({
      req: "hub.sync",
    });
  }, 1000);
}

main();
