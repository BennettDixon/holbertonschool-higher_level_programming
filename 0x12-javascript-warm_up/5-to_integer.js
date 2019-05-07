#!/usr/bin/node
const process = require('process');
let resp;
let num;
resp = 'Not a number';
if (process.argv.length > 2) {
  num = parseInt(process.argv[2]);
  if (!isNaN(num)) {
    resp = 'My number: ' + String(num);
  }
}
console.log(resp);
