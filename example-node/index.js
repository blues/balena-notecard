const axios = require("axios");

async function makeRequest(json) {
  try {
    const resp = await axios.post(
      "http://notecard:3434",
      JSON.stringify(json),
      {
        headers: {
          "Content-Type": "application/json",
        },
      }
    );
    console.log("Successful request");
    console.log(resp.data);
  } catch (e) {
    console.log("Request did not work when trying to send", json);
    console.log("Error", e.message);
  }
}

async function main() {
  makeRequest({
    req: "hub.set",
    product: "com.blues.tvantoll:weather",
  });

  setTimeout(() => {
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
