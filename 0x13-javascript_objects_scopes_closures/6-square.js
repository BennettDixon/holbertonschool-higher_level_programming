#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
  charPrint (c) {
    this.print(c);
  }
}
module.exports = Square;
