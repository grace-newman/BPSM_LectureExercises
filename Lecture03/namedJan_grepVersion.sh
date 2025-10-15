#!/usr/bin/bash
cat cleaned_example_people_data.tsv | cut -f1 | grep -wc "Jan" #grep whole words only and output a count
