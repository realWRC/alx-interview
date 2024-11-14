#!/usr/bin/env node
// Script that prints all characters of a Star Wars movie in order

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

request(url, async function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const film = JSON.parse(body);
  const characters = film.characters;

  for (const characterUrl of characters) {
    await new Promise((resolve, reject) => {
      request(characterUrl, function (charError, charResponse, charBody) {
        if (charError) {
          console.error(charError);
          reject(charError);
        } else {
          const character = JSON.parse(charBody);
          console.log(character.name);
          resolve();
        }
      });
    });
  }
});
