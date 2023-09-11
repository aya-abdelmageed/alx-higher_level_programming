#!/usr/bin/node
//  prints My number: <first argument converted in integer>
//  in the given format

if (isNaN(process.arg[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(process.argv[2]));
}
