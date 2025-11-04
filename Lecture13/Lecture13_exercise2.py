#!/usr/bin/python3

# Lecture 13, Exercise 2: Multiple exons from genomic DNA
# Written by Grace Newman (s2823303) on 31 October 2025

# A python script that extracts the exon segments from a file containing genomic dna, concatenates them, and writes them to a new file.

# Open the input files
genomic_dna = open("genomic_dna2.txt").read().rstrip()
exon_lines = open("exons.txt").readlines() # read each line separately

# Create an empty list for the exon segment strings
exon_segments = []

# Process each row
for eachrow in exon_lines:
	exon_list = eachrow.rstrip().split(",") # convert each row to a list of the start and stop positions
	exon_sequence = genomic_dna[((int(exon_list[0]))-1):int(exon_list[1])] # slice the genomic_dna based on the list of start and stop positions (stop positions should be included)
	exon_segments.append(exon_sequence) # append each exon to a list

print(exon_segments)
s = ""
coding_dna = s.join(exon_segments) # join the list of exon segments into one string

# Write the coding sequence to a file
output_file = open("exercise2_output.dna", "w")
output_file.write(coding_dna)
output_file.close()
