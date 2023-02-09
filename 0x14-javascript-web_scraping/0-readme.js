#!/usr/bin/node
// reads and prints the contents of a file.

const fs = require('fs');
const filePath = process.argv[2];

fs.readFile(filePath, { encoding: 'utf8' }, (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
