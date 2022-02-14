const axios = require("axios");

async function main() {
  let random = 0;

  while (true) {
    try {
      const json = `{"number": ${random}}`;
      await axios.post("http://notecard:8080", json, {
        headers: {
          "Content-Type": "application/json",
        },
      });
      random = random + 1;
    } catch (e) {
      console.log("Post did not work");
      console.log(e.message);
    }
    console.log("posted: " + random);
    await new Promise((r) => setTimeout(r, 10000));

    // Sync after 5 calls
    if (random > 5) {
      random = 0;
      await axios.post("http://notecard:8080/sync");
      console.log("performed sync");
    }
  }
}

main();
