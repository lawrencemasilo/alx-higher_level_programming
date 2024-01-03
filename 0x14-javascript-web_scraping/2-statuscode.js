#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (err, response) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
  console.log(`code: ${response.statusCode}`);
});
