#!/usr/bin/bash

cat cleaned_example_people_data.tsv | awk 'BEGIN{FS="\t";}{if($1=="Jan"){print $0;}}' | wc -l
