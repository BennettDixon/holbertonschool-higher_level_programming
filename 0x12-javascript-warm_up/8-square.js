#!/usr/bin/node
const process = require('process');
let build = '';
let failed = 'Missing size';
let num;
let i;
let j;

if (process.argv.length > 2) {
  num = parseInt(process.argv[2]);
  if (isNaN(num)) {
    build = failed;
  } else {
    for (i = 0; i < num; i++) {
      if (i > 0) {
        build += '\n';
      }
      for (j = 0; j < num; j++) {
        build += 'X';
      }
    }
  }
} else {
  build = failed;
}
if (build !== '') {
  console.log(build);
}
