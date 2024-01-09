#!/usr/bin/node

function factorial (num) {
  if (isNaN(num) || num <= 1) {
    return 1;
  }

  return num * factorial(num - 1);
}

const arg = parseInt(process.argv[2], 10);

console.log(factorial(arg));
