#!/usr/bin/node
// import { argv } from 'node:process';
// const argv = require('node:process').argv;

if (process.argv[3]) {
  console.log('Arguments found');
} else if (process.argv[2]) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
