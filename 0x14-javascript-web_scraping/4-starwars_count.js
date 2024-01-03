#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }

  try {
    const films = JSON.parse(body).results;
    const wedge = films.filter((film) =>
      film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
    );
    console.log(`${wedge.length}`);
  } catch (parseError) {
    console.error(parseError);
    process.exit(1);
  }
});
