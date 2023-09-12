#!/usr/bin/node
// func that returns the reversed version of a list

exports.esrever = function (list) {
  const ans = [];
  const l = list.length - 1;
  for (let i = l; i >= 0; i--) {
    ans.push(list[i]);
  }
  return (ans);
};
