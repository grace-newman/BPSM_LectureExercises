#!/usr/bin/bash

cat cleaned_example_people_data.tsv | awk 'BEGIN{FS="\t";}{if($6<=1995){print $0;}}' | wc -l
