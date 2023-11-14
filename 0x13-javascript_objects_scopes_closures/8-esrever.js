#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  let i = list.length - 1;

  while (i > -1) {
    newList.push(list[i]);
    i--;
  }
  return newList;
};
