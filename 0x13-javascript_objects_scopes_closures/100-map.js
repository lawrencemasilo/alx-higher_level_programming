#!/usr/bin/node
const list = require('./100-data.js');

const outList = list.list;
console.log(outList);
const newList = list.list.map((element, index) => element * index);
console.log(newList);
