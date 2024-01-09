#!/usr/bin/node

function addMeMaybe (number, theFunction) {
  let increment = number + 1;
  theFunction(increment);
}

module.exports = {
  addMeMaybe: addMeMaybe
};
