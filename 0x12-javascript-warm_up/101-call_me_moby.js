#!/usr/bin/node

function callMeMoby (x, theFunction) {
  if (x <= 0) return;

  function exe (n) {
    if (n > 0) {
      theFunction();
      exe(n - 1);
    }
  };

  exe(x);
}
