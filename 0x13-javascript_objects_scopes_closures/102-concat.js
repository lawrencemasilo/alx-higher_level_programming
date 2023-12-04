#!/usr/bin/node

const files = require('fs');
const fA = files.readFileSync(process.argv[2]).toString();
const sA = files.readFileSync(process.argv[3]).toString();
files.writeFileSync(process.argv[4], fA + sA);
