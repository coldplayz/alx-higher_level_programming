#!/usr/bin/node
/*
 * Prints the title of a Star Wars movie where the episode number matches a given integer.
 *   - The first argument is the movie ID.
 *   - You must use the Star wars API with the endpoint https://swapi-api.alx-tools.com/api/films/:id.
 *   - You must use the module request.
*/

const request = require('request');
const filmID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmID}`;

// Make request
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    // Retrieve json from body
    if (typeof body === 'string') {
      body = JSON.parse(body);
    }
    // Print title of film episode
    const title = body.title;
    console.log(`${title}`);
  }
});
