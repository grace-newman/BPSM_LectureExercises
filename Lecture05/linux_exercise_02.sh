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
			if test ${birthday_year} -gt 1995
			then
			echo -e "X\tYounger than 30"
	else
		count=$((count+1))
		echo -e "${count}\t${birthday_year}"
fi # a real country
fi # a blank line
fi # a person born after 1995
done < example_people_data.tsv
