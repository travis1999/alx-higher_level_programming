exports.nbOccurences = function (list, searchElement) {
  let occur = 0;
  list.forEach(x => {
    if (x === searchElement) {
      occur += 1;
    }
  });

  return occur;
}
