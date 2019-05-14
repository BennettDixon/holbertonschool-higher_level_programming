#!/usr/bin/node
const process = require('process');
const request = require('request');

let episode = parseInt(process.argv[2]);
let url = 'http://swapi.co/api/films/';
let data;

request(url, function (error, response, body) {
  if (error != null) {
    console.log(error);
  } else {
    console.log(body);
    data = JSON.parse(body);
    let counter = 1;
    data['results'].forEach(function (obj) {
      if (counter === episode) {
        console.log(obj['title']);
      }
      counter++;
    });
  }
});
