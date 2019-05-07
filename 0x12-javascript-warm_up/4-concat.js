#!/usr/bin/node
const process = require('process');

let resp;
resp = '';
process.argv.forEach(function (value, index) {
  if (index > 1) {
    if (index > 2) {
      resp += ' ';
    }
    resp += value;
  }
});
console.log(resp);
