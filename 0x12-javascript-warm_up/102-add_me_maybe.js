#!/usr/bin/node

function addMeMaybe (number, theFunction) {
  increment = number + 1;
  theFunction(increment);
}

module.exports = {
  addMeMaybe: addMeMaybe
};
