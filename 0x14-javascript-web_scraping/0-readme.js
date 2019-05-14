#!/usr/bin/node
const process = require('process');
const filesystem = require('fs');

let file = process.argv[2];

filesystem.readFile(file, 'utf8', function (err, data) {
  if (err != null) {
    console.log(err);
  } else {
    process.stdout.write(data);
  }
});
