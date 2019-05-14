#!/usr/bin/node
const square = require('./5-square');
class Square extends square {
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
