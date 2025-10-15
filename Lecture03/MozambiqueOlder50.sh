#!/usr/bin/bash

cat cleaned_example_people_data.tsv | awk 'BEGIN{FS="\t"}{if($7=="Mozambique" && $6 <= 1975){print $1,$6;}}'
