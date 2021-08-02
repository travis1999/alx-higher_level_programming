#!/usr/bin/node
const process = require('process');

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let idy = 0; idy < parseInt(process.argv[2]); idy++) {
    for (let index = 0; index < parseInt(process.argv[2]); index++) {
      process.stdout.write('X');
    }
    console.log();
  }
}
