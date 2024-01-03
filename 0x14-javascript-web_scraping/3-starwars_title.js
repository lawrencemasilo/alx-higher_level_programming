#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const api = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(api, (err, response, body) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }

  try {
    const movie = JSON.parse(body);
    console.log(`${movie.title}`);
  } catch (parseError) {
    console.error(parseError);
    process.exit(1);
  }
});
