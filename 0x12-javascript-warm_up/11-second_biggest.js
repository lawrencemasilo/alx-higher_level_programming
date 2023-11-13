#!/usr/bin/node

const array = process.argv.slice(2).map(Number);

if (array < 2) {
  console.log(0);
} else {
  array.sort((a, b) => b - a);
  console.log(Number(array[1]));
}
