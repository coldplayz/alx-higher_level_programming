#!/usr/bin/node
/*
 * Display the status code of a GET request:
 *   The first argument is the URL to request (GET)
 *   The status code must be printed like this: code: <status code>
 *   You must use the module request.
*/

const request = require('request');
const url = process.argv[2];

// Make request
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  console.log(`code: ${response.statusCode}`);
});
