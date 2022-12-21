#!/usr/bin/node
// defines a square and inherits from Rectangle of 4-rectangle.js.

const Square1 = require('./5-square.js');

class Square extends Square1 {
  charPrint (c) {
    for (let i = 0; i < this.width; i++) {
      console.log((c || 'X').repeat(this.width));
    }
  }
}

module.exports = Square;
