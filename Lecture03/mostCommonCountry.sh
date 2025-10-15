#!/usr/bin/bash

cat cleaned_example_people_data.tsv | cut -f7 | sort | uniq -c | sort -k1,1nr | head -n3
