#!/usr/bin/node
// returns the reversed version of a list.

exports.esrever = function (list) {
  let reversed = [];
  const arrLen = list.length;

  for (let i = arrLen - 1; i <= 0; i++) {
    reversed.push(list[i]);
  }
  return reversed;
};
