#!/usr/bin/node

const fs = require('fs');

fileName = process.argv[2];

fs.readFile(fileName, 'utf-8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(data);
});
