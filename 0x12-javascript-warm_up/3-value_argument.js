#!/usr/bin/node
const process = require('process');
let arg = process.argv[2];
if (arg === undefined) {
  console.log('No argument');
} else {
  console.log(arg);
}
