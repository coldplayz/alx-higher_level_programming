#!/usr/bin/node
// import { argv } from 'node:process';
const argv = require('node:process').argv;

if (argv[3]) {
  console.log('Arguments found');
} else if (argv[2]) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
