#!/usr/bin/node
// defines a square and inherits from Rectangle of 4-rectangle.js.

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let i = 0; i < this.width; i++) {
      console.log((c || 'X').repeat(this.width));
    }
  }
}

module.exports = Square;
