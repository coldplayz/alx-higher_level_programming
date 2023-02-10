#!/usr/bin/node
/**
 * Prints all characters of a Star Wars movie:
 *   - The first argument is the Movie ID - example: 3 = “Return of the Jedi”
 *   - Display one character name by line.
 *   - You must use the Star wars API.
 *   - You must use the module request.
 */

const id = process.argv[2];
const url = 'http://swapi.co/api/films/' + id;
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    console.log('Req. 1');
    body = JSON.parse(body);
    for (const i in body.characters) {
      request(body.characters[i], function (err, response, body) {
        if (err) {
          console.error(err);
        } else if (response.statusCode === 200) {
          console.log(JSON.parse(body).name);
	}
      });
    }
  }
});
