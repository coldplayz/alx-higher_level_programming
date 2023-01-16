#!/usr/bin/env bash


hdr='size: 10'
hdr2=${hdr#size*:}
hdr3=" 10 "
hdr4=$(echo $hdr3)
echo "$hdr3"
len1=${#hdr3}
len2=0

#while [ ("$len1" - "$len2") -gt 0 ]
while (( len1 - len2 > 0 ))
do
	len1=${#hdr3}

	hdr3="${hdr3# }"
	hdr3="${hdr3% }"

	len2=${#hdr3}
done

echo "$hdr3"
