#!/usr/bin/node

function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}
