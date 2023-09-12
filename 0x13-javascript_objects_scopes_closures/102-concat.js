#!/usr/bin/node
// a script that concats 2 files.

const f = require('fs');
const a = f.readFileSync(process.argv[2], 'utf8');
const b = f.readFileSync(process.argv[3], 'utf8');
f.writeFileSync(process.argv[4], a + b);
