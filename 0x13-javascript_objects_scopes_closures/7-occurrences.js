#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, currentElement) => {
    return count + (currentElement === searchElement ? 1 : 0);
  }, 0);
};
