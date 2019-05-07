#!/usr/bin/node

let languages = ['C is fun', 'Python is cool', 'Javascript is amazing'];
let resp = '';
languages.forEach(function (value, index) {
  if (index > 0) {
    resp += '\n';
  }
  resp += value;
});
console.log(resp);
