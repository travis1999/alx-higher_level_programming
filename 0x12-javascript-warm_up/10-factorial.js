#!/usr/bin/node
const argv = require('process').argv;

function factorial (number) {
  if (isNaN(number) || number === 1) {
    return 1;
  }

  if (number <= 0) {
    return (0);
  }

  return number * factorial(number - 1);
}

console.log(factorial(parseInt(argv[2])));
