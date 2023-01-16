#!/usr/bin/env bash
# Takes in a URL, sends a request to that URL, and displays the size of the body of the response.

# Get the response header only
hdr=$(curl -Is "$1")

IFS=$'\r\n' # also necessary for CRLF
for line in $hdr
do
	#line=${line@L} # convert line to lowercase
	hdrline=${line%%:*} # get longest match
	#echo $hdrline
	if [[ "$hdrline" = 'Content-Length' ]]
	then
		# Extract the header value
		data=${line#Content-Length*:}

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
