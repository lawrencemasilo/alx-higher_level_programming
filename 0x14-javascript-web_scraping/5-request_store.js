#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];

request.get({ url, encoding: 'utf-8' }, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  fs.writeFile(process.argv[3], body, 'utf-8', (writeError) => {
    if (writeError) {
      console.error(writeError);
      process.exit(1);
    }
  });
});
