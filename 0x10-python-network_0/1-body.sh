#!/usr/bin/env bash
# bash script to send a get request to the url and display body of resposne
URL=$1
STATUS=$(curl -LIs $URL | grep 'HTTP/' | cut -f2 -d' ')
SUCCESS='FALSE'
for i in $STATUS; do
	if [ "$i" -eq '200' ]; then
		SUCCESS='TRUE'
	fi
done
if [ "$SUCCESS" == 'TRUE' ]; then
	curl -L $URL
else
	echo 'status not 200'
fi
