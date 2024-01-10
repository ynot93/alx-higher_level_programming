#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};

for (const userId in dict) {
  const occurences = dict[userId];

  if (!newDict[occurences]) {
    newDict[occurences] = [];
  }
  newDict[occurences].push(userId);
}
console.log(newDict);
