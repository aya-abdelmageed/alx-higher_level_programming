#!/usr/bin/node
// a script that imports an array and computes a new array

const list = require('./100-data.js').list;
console.log(list);
console.log(list.map((n, i) => n * i));
