#!/usr/bin/node
/**
 * Prints all characters of a Star Wars movie:
 *   - The first argument is the Movie ID - example: 3 = “Return of the Jedi”
 *   - Display one character name by line.
 *   - You must use the Star wars API.
 *   - You must use the module request.
 *
 * Algorithm employed:
 * 1. Create a global object - resultsObj - to hold the mapping between a character and its URL.
 * 2. Get the list of character URLs in the body.characters of the first request.
 * 3. Save the length of the characters list, and the list itself, for reference in the scope of the subsequent request.
 * 4. Iterate over the character URLs list, making a request on each. For each request, create a mapping of the request URL and the scraped character name in the resultsObj object.
 * 5. Also, for each of these iterations, perform a check to know when the last URL/API in the list has been requested. If last, then use the resultsObj mapping to display the names in order.
 */

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
const request = require('request');

const resultsObj = {};

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    body = JSON.parse(body);
    const lenBody = body.characters.length;
    const charURLS = body.characters;
    for (const i in body.characters) {
      const characterURL = body.characters[i];
      request(characterURL, function (err, response, body) {
        if (err) {
          console.error(err);
        } else if (response.statusCode === 200) {
          body = JSON.parse(body);
          resultsObj[body.url] = body.name;
          if (Object.keys(resultsObj).length === lenBody) {
            for (const actorURL of charURLS) {
              console.log(resultsObj[actorURL]);
            }
          }
        }
      });
    }
  }
});
