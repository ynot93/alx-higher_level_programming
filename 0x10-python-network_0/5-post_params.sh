#!/bin/bash
# Send POST request with parameters email and subject
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" $1
