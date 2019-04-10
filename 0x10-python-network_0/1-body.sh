#!/usr/bin/env bash
# bash script to send a get request to the url and display body of resposne
URL=$1
STATUS=$(curl -Is $URL | head -n1 | cut -f2 -d' ')
if [ "$STATUS" -eq '200' ]; then
	curl $URL
fi
