#!/usr/bin/node
// a script that imports a dictionary of occurrences by user id
// and computes a dictionary of user ids by occurrence

const d = require('./101-data.js').dict;
const ans = {};

for (const k in d) {
  const i = d[k];
  ans[i] = [];
  for (const x in d) {
    if (d[x] === i) {
      ans[i].push(x);
    }
  }
}
console.log(ans);
