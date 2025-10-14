#!/usr/bin/bash

IFS="/><"

beast="Cosmoscarta"
db="nucleotide"

efetchstuff=$(wget -qO- "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nucleotide&term=Cosmoscarta&usehistory=y" \
| egrep "QueryKey|WebEnv")

QueryKey=$(echo ${efetchstuff} | awk '{print $(NF-5)}')
echo ${QueryKey}

WebEnv=$(echo ${efetchstuff} | awk '{print $(NF-2)}')
echo ${WebEnv}

unset IFS

wget -qO cosmoscarta_sequences.fasta \
"http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=${db}&query_key=${QueryKey}&WebEnv=${WebEnv}&rettype=fasta&retmode=text"
