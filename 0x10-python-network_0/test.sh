#!/usr/bin/env bash

# Get the response header only
hdr=$(curl -Is www.google.com)

IFS=$'\r\n' # also necessary for CRLF
for line in $hdr
do
	line=${line@L} # convert line to lowercase
	hdrline=${line%%:*} # get longest match
	#echo $hdrline
	if [[ "$hdrline" = 'x-xss-protection' ]]
	then
		# Extract the header value
		data=${line#x-xss-protection*:}

		# Remove all leading an trailing whitespaces
		len1=${#data}
		len2=0
		while (( len1 - len2 > 0 ))
		do
			len1=${#data}
			data=${data# } # remove leading whitespace
			data=${data% } # remove trailing whitespace
			len2=${#data}
		done
		echo "$data"
		break
	fi
done
