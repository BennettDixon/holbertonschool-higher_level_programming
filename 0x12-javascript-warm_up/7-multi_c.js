#!/usr/bin/node
const process = require('process');
let build = '';
let failed = 'Missing number of occurrences';
let num;
let i;

if (process.argv.length > 2) {
  num = parseInt(process.argv[2]);
  if (isNaN(num)) {
    build = failed;
  } else {
    for (i = 0; i < num; i++) {
      if (i > 0) {
        build += '\n';
      }
      build += 'C is fun';
    }
  }
} else {
  build = failed;
}
if (build !== '') {
  console.log(build);
}
