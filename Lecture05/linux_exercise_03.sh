#!/bin/bash

count=0
unset IFS
IFS=$'\t'

while read name email city birthday_day birthday_month birthday_year country
do
	if test -z ${name}
	then
	echo -e "X\tBlank line found"
	else
		if test ${country} == "country"
		then
		echo -e "X\tHeader line found"
		else
			if test ${name} != "Jan"
			then
			echo -e "X\tTheir name is not Jan it is: ${name}"
	else
		count=$((count+1))
		echo -e "${count}\tYay! We found ${name}"
fi # a real country
fi # a blank line
fi # a person not named Jan
done < example_people_data.tsv
