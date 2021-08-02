#!/usr/bin/node
const argv = require('process').argv;

if (argv.length === 2 || argv.length === 3) {
  console.log(0);
} else {
  const slice = argv.slice(2);
  const n = slice.sort(function (a, b) { return a - b; });
  console.log(n[n.length - 2]);
}
