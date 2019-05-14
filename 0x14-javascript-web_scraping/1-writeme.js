#!/usr/bin/node
const process = require('process');
const filesystem = require('fs');

let file = process.argv[2];
let text = process.argv[3];

filesystem.writeFile(file, text, 'utf8', function (err, data) {
  if (err != null) {
    console.log(err);
  }
});
