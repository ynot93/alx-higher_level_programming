#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const characterId = '18';
let count = 0;

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const allFilms = JSON.parse(body).results;

  for (const film of allFilms) {
    for (const character of film.characters) {
      if (character.includes(characterId)) {
        count += 1;
      }
    }
  }
  console.log(count);
});
