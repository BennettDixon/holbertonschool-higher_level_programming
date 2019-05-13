#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i;
    let j;
    let build = '';
    for (i = 0; i < this.height; i++) {
      if (i > 0) {
        build += '\n';
      }
      for (j = 0; j < this.width; j++) {
        build += 'X';
      }
    }
    console.log(build);
  }
}
module.exports = Rectangle;
