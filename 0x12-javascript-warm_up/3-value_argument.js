#!/usr/bin/node
const argv = require('process').argv;
const first = argv[2];

if (first === undefined) {
  console.log('No argument');
} else {
  console.log(first);
}
