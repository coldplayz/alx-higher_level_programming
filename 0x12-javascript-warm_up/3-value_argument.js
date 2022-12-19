#!/usr/bin/node
// Prints the first argument passed to it.

// const argv = require('node:process').argv;

if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
