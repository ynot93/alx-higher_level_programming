#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const characterId = 18;
const characterUrl = `https://swapi-api.alx-tools.com/api/people/${characterId}/`;

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const allFilms = JSON.parse(body).results;

  const wedgeFilms = allFilms.filter(film =>
    film.characters.includes(characterUrl)
  );

  console.log(wedgeFilms.length);
});
