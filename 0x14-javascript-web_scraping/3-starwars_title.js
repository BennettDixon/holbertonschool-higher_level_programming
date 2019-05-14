#!/usr/bin/node
const process = require('process');
const request = require('request');

let episode = process.argv[2];
let url = 'http://swapi.co/api/films/';
let data;

request(url, function (error, response, body) {
  data = JSON.parse(body);
  data['results'].forEach(function(obj) {
    let ep_id = obj['episode_id'].toString(10);
    if (ep_id === episode) {
      console.log(obj['title']);
      process.exit(0);
    }
  });
});
