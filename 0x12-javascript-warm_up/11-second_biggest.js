#!/usr/bin/node

const args = process.argv.slice(2);

if (args <= 1) {
  console.log('0');
} else {
  console.log(secondBiggest(args));
}

function secondBiggest (arr) {
  const sortedUnique = [...new Set(arr)].sort((a, b) => b - a);
  return sortedUnique[1];
}
