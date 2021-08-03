#!/usr/bin/node

exports.esrever = function (list) {
  const newarr = [];

  for (let i = list.length - 1; i >= 0; i--) {
    newarr.push(list[i]);
  }

  return newarr;
};
