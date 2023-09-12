#!/usr/bin/node
// func to print the number of arguments already printed
// and the new argument value

let c = 0;
exports.logMe = function (item) {
  console.log(c + ': ' + item);
  c++;
};
