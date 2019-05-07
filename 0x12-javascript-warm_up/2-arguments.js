#!/usr/bin/node
const process = require('process');
let resp;
if (process.argv.length > 2) {
	resp = "Arguments found";
}
else {
	resp = "No argument";
}
console.log(resp);
