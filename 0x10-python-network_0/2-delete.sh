#!/bin/bash
# script to send delete request to the url passed and displays reponse
curl -L -X 'DELETE' "$1"
