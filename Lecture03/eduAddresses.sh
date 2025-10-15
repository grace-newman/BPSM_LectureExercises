#!/usr/bin/bash

cat cleaned_example_people_data.tsv | grep "\.edu" | sort -t $'\t' -k7,7 -k1,1r | cut -f1,7,2
