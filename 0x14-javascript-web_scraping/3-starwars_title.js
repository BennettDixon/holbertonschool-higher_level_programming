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
    data = JSON.parse(body);
    data['results'].forEach(function (obj) {
      let epId = obj['episode_id']
      if (epId === episode) {
        console.log(obj['title']);
      }
    });
  }
});
