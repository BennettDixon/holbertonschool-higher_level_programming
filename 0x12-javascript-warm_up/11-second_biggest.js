#!/usr/bin/node
const process = require('process');
let max;
let secondMax;

process.argv.forEach(function (value, index) {
  value = parseInt(value);
  if (index > 1) {
    if (max === undefined) {
      max = value;
    } else if (secondMax === undefined && value <= max) {
      secondMax = value;
    } else if (value >= max) {
      secondMax = max;
      max = value;
    }
  }
});
if (secondMax === undefined) {
  console.log(0);
} else {
  console.log(secondMax);
}
