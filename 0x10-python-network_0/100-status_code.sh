#!/bin/bash
# bash script to display status code of server
curl -L -s -X HEAD -w "%{http_code}" "$1"
