#!/usr/bin/node
// computes and prints a factorial

function fact (x) {
  if ((isNaN(x)) || (x === 1)) {
    return 1;
  } else {
    return x * fact(x - 1);
  }
}

console.log(fact(parseInt(process.argv[2])));
