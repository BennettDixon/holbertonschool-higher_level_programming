#!/usr/bin/node
const process = require('process');
let resp;
if (process.argv.length === 3) {
  resp = 'Argument found';
} else if (process.argv.length < 3) {
  resp = 'No argument';
} else {
  resp = 'Arguments found';
}
console.log(resp);
