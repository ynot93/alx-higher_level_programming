#!/bin/bash
# Display HTTP methods the server accepts 
curl -sI -X OPTIONS $1 | grep -i Allow | cut -d ' ' -f2-
