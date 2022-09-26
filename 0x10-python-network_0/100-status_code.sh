#!/bin/bash
#Sends a request to a URL passed as an argument, displays only the status code
curl -sI -o /dev/null -w '%{http_code}' "$1"
