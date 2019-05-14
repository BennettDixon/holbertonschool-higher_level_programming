#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
  charPrint (c) {
    if (typeof c === 'undefined') {
      c = 'X';
    }
    this.print(c);
  }
}
module.exports = Square;
