#!/usr/bin/node
const process = require('process');

function factorialize (num) {
  if (isNaN(num)) {
    return 1;
  }
  if (num < 0) {
    return -1;
  } else if (num === 0) {
    return 1;
  } else {
    return (num * factorialize(num - 1));
  }
}

console.log(factorialize(parseInt(process.argv[2])));
