#!/usr/bin/node
// reads and prints the contents of a file.

const fs = require('fs').promises;
const filePath = process.argv[2];

async function readf (filePath) {
  try {
    const data = await fs.readFile(filePath, { encoding: 'utf8' });
    console.log(data.toString());
  } catch (error) {
    console.error(error);
  }
}

readf(filePath);
