#!/usr/bin/node
const process = require('process');
const request = require('request');

let url = process.argv[2];
let data;

request(url, function (error, response, body) {
  if (error != null) {
    console.log(error);
  } else {
    let movies = 0;
    data = JSON.parse(body);
    data['results'].forEach(function (result) {
      result['characters'].forEach(function (character) {
        let urlSplit = character.split('/');
        if (urlSplit[urlSplit.length - 2] === '18') {
          movies++;
        }
      });
    });
    console.log(movies);
  }
});
