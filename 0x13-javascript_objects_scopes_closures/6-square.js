const Sq = require('./5-square');

class Square extends Sq {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let y = 0; y < this.height; y++) {
      for (let x = 0; x < this.width; x++) {
        process.stdout.write(c);
      }
      console.log();
    }
  }
}

module.exports = Square;
