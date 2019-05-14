#!/usr/bin/node
const process = require('process');
const request = require('request');

let movie = process.argv[2];
let url = 'https://swapi.co/api/films/' + movie;

function printCharName (charUrl) {
  request(charUrl, function (error, response, body) {
    if (error != null) {
      console.log(error);
    } else {
      let data = JSON.parse(body);
      console.log(data['name']);
    }
  });
}

request(url, function (error, response, body) {
  if (error != null) {
    console.log(error);
  } else {
    let data = JSON.parse(body);
    data['characters'].forEach(function (charUrl) {
      printCharName(charUrl);
    });
  }
});
