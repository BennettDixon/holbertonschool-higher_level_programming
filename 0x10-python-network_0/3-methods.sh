#!/bin/bash
# script to get the allowed methods in an server if availaible through OPTIONS http request
curl -s -I -X OPTIONS "$1" | grep 'Allow:' | cut -f2- -d' '
