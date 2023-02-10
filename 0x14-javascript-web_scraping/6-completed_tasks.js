#!/usr/bin/node
/*
 * Computes the number of tasks completed by user id.
 *   - The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
 *   - Only print users with completed task.
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
    // body is a list of todos dictionaries
    const resultsObj = {};
    for (const dict of body) {
      if (typeof resultsObj[dict.userId] === 'undefined') {
        // Initialize the property
        resultsObj[dict.userId] = 0; // initialize count
      }
      if (dict.completed) {
        resultsObj[dict.userId] += 1;
      }
    }
    // Remove users with zero completed tasks
    for (const uID in resultsObj) {
      if (resultsObj[uID] === 0) {
        delete resultsObj[uID];
      }
    }
    console.log(resultsObj);
  }
});
