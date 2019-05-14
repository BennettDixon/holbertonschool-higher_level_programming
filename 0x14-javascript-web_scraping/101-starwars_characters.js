#!/usr/bin/node
const process = require('process');
const request = require('request');
let order = [];
let responses = {};

function getCharName (charUrl) {
  let val;
  val = request(charUrl, function (error, response, body) {
    if (error != null) {
      console.log(error);
    } else {
      let data = JSON.parse(body);
      val = data['name'];
      responses[charUrl] = val;
    }
  });
}

function doParse () {
  let movie = process.argv[2];
  let url = 'https://swapi.co/api/films/' + movie;

  request(url, function (error, response, body) {
    if (error != null) {
      console.log(error);
    } else {
      let data = JSON.parse(body);
      data['characters'].forEach(function (charUrl) {
        order.push(charUrl);
        getCharName(charUrl);
      });
    }
  });
}

doParse();
setTimeout(function () {
  // some stuff
  order.forEach(function (url) {
    console.log(responses[url]);
  });
}, 5000);
