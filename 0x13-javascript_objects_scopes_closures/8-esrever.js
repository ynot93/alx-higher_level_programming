#!/usr/bin/node

exports.esrever = function (list) {
  return list.reduce((reversedList, currentElement) => {
    reversedList.unshift(currentElement);
    return reversedList;
  }, []);
};
