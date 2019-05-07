#!/usr/bin/node
const process = require('process');

let val1;
let val2;
if (process.argv.length > 2) {
  if (process.argv.length > 3) {
    val2 = process.argv[3];
  }
  val1 = process.argv[2];
}
console.log(val1 + ' is ' + val2);
