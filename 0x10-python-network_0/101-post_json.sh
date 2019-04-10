#!/bin/bash
# bash script for posting json data files and testing a server
curl -d "@$2" -H "Content-Type: application/json" -X POST "$1"
