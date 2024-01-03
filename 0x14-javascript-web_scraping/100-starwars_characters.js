#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  try {
    JSON.parse(body).characters.forEach((characterURL) => {
      request.get(characterURL, (err, res, data) => {
        if (err) {
          console.error(err);
          return;
        }
        console.log(JSON.parse(data).name);
      });
    });
  } catch (parseError) {
    console.error(parseError);
    process.exit(1);
  }
});
