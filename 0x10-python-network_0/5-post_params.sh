#!/bin/bash
# script to post data (url-encoded) to a server
curl -d "email=hr@holberotnschool.com&subject=I%20will%20always%20be%20here%20for%20PLD" -X POST "$1"
