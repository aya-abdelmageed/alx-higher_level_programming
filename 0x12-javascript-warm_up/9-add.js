#!/usr/bin/node
// print the addition of 2 integers

// fun to add to num

function add (a, b) {
  return (a + b);
}

console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])));
