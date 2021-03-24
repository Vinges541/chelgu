#!/bin/bash
if [ "$#" -ne 4 ]

then
	echo "Usage: $0 height width fill(0/1) fillchar"
	exit 1
fi

height=$1
width=$2
fill=$3
fillchar=$4

for (( i = 1; i <= $height; i++ ))
do

	for (( j = 1; j <= $width; j++ ))
	do

		if [ "$i" -eq 1 -o "$i" -eq "$height" -o "$j" -eq 1 -o "$j" -eq "$width" -o "$fill" -eq 1 ] 
		then 
			echo -n "$fillchar"
		else
			echo -n " "
		fi
        
	done

	echo

done