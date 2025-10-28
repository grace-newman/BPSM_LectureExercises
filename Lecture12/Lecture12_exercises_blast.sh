#!/usr/bin/bash

# A script to run a blastx (DNA query vs a protein database) against our nem database from Lecture 6

db="/localdisk/home/s2823303/Exercises/Lecture06/nem" # create a variable for the database
queryseqs="All_exons.fasta" # variable for the file of all the exons
blastx -db ${db} -query ${queryseqs} -outfmt 7 | head -n6


# Modify the search parameters to change the output from BLAST
# -outfmt 6 gives us the tabulated format, but no headings
# -num_alignments 1 will give us only the single best alignment for each of our three exon sequences
blastx -db ${db} -query ${queryseqs} -outfmt 6 -num_alignments 1 > quick_blast_check.out
