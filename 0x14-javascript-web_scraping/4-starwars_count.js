#!/usr/bin/node
const process = require('process');
const request = require('request');

let urlType = process.argv[2];
let url = 'http://swapi.co/api/people/18';
let data;

request(url, function (error, response, body) {
  if (error != null) {
    console.log(error);
  } else {
    data = JSON.parse(body);
    console.log(data['films'].length);
  }
});
