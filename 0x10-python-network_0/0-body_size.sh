#!/usr/bin/bash
# Sends request to URL and displays the size of the body
# of the response

if [ -z "$1" ]; then
  echo "Usage: "$0" <url>"
  exit 1
fi

curl -sI "$1" | grep Content-Length | awk '{print $2}'
