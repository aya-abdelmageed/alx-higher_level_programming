#!/usr/bin/node
// func that returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  return list.reduce((c, i) => i === searchElement ? c++ : c, 0);
};
