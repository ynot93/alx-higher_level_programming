#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const allFilms = JSON.parse(body).results;

  const wedgeFilms = allFilms.filter(film =>
    film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
  );

  console.log(wedgeFilms.length);
});
