#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const movie = JSON.parse(body);

  const characterLinks = movie.characters;
  const characterPromises = characterLinks.map(characterLink => {
    return new Promise((resolve, reject) => {
      request.get(characterLink, (err, response, body) => {
        if (err) {
          reject(err);
          return;
        }
        const character = JSON.parse(body);
        resolve(character.name);
      });
    });
  });

  Promise.all(characterPromises)
    .then(characters => {
      characters.forEach(character => {
        console.log(character);
      });
    })
    .catch(err => {
      console.log(err);
    });
});
