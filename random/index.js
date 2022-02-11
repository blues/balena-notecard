const axios = require("axios");
let random = 0;

async function main() {
  while (true) {
    try {
      await axios.post("http://192.168.4.64:8080/send", {
        number: random,
      });
      random = random + 1;
    } catch (e) {
      console.log("post did not work");
      console.log(e.message);
    }
    console.log("posted: " + random);
    await new Promise((r) => setTimeout(r, 10000));
  }
}

main();
