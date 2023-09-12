#!/usr/bin/node
// func to convert a number from base 10 to another base passed as argument

exports.converter = function (base) {
  return x => x.toString(base);
};
