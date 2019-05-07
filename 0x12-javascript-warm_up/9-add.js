#!/usr/bin/node
const process = require('process');
let resp;
let num;
let num2;
resp = 'NaN';

if (process.argv.length > 3) {
  num = parseInt(process.argv[2]);
  num2 = parseInt(process.argv[3]);
  if (!isNaN(num) && !isNaN(num2)) {
    resp = String((num + num2));
  }
}
console.log(resp);
