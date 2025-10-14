#!/usr/bin/bash

while read accession
	do
	echo -e "Downloading ${accession} ..."
	wget -O ${accession}.fasta \
	"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id=${accession}&strand=1&rettype=fasta&retmode=text"
	done < myfileofaccessions.txt
