#!/usr/bin/node

if (Number(process.argv[2])) {
  for (let i = 1; i <= Number(process.argv[2]); i++) {
    let row = '';
    for (let j = 1; j <= Number(process.argv[2]); j++) {
      row += 'x';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
