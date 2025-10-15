#!/usr/bin/bash
rm cleaned_example_people_data.tsv # remove old/previous file
cat example_people_data.tsv | awk 'BEGIN{FS="\t";}{if(NF==7 && $1 != "name"){print $0;}}' >> cleaned_example_people_data.tsv # append the line to a new file
cat cleaned_example_people_data.tsv | cut -f1 | wc -l # cut field 1 from each column and count the number of lines
