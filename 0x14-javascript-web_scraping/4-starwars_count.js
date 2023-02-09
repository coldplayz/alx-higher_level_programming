#!/usr/bin/node
/*
 * Prints the number of movies where the character “Wedge Antilles” is present.
 *   - The first argument is the API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/
 *   - Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
 *   - You must use the module request.
*/

const request = require('request');
const url = process.argv[2];

// Make request
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    // Retrieve json from body
    if (typeof body === 'string') {
      body = JSON.parse(body);
    }
    // Retrieve number of films of character
    let moviesActed = 0;
    const results = body.results; // contains list of film dictionaries
    for (const film of results) {
      const characterURLS = film.characters;
      for (const characterURL of characterURLS) {
        if (characterURL.endsWith('18/')) {
          moviesActed += 1;
        }
      }
    }
    console.log(`${moviesActed}`);
  }
});
