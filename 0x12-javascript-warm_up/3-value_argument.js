#!/usr/bin/node
const process = require('process');
let resp;
if (process.argv.length > 2) {
  resp = process.argv[2];
} else {
  resp = 'No argument';
}
console.log(resp);
