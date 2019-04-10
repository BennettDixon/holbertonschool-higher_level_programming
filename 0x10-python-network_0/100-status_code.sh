#!/bin/bash
# bash script to send a get request to the url and display body of resposne
# shellcheck disable=SC2046
curl -L -s -X HEAD -w "%{http_code}" "$1"
