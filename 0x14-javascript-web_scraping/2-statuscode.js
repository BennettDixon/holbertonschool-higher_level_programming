#!/usr/bin/node
const process = require('process');
const filesystem = require('fs');
const request = require('request');

let url = process.argv[2];

request(url, function (error, response, body) {
  console.log('code:', response.statusCode);
});
