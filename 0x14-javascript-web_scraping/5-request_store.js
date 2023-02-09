#!/usr/bin/node
/*
 * Gets the contents of a webpage and stores it in a file.
 *   - The first argument is the URL to request.
 *   - The second argument the file path to store the body response.
 *   - The file must be UTF-8 encoded.
 *   - You must use the module request.
*/

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

// Make request
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    /*
    // Retrieve json from body
    if (typeof body === 'string') {
      body = JSON.parse(body);
    }
    */

    // Write body to file
    fs.writeFile(filePath, body, { encoding: 'utf8' }, err => {
      if (err) {
        console.error(err);
      }
    });
  }
});
