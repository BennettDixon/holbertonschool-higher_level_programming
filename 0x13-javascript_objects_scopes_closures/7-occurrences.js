#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  list.forEach(function (obj) {
    if (obj === searchElement) {
      i++;
    }
  });
  return i;
};
