#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that causes the output "You got me!"
curl -sI -X OPTIONS 0.0.0.0:5000/catch_me
