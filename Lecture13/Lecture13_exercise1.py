#!/usr/bin/bash

# Lecture 13, Exercise 1: Processing DNA in a file
# Written by Grace Newman (s2823303) on 31 October 2025

# The file input.txt contains a number of DNA sequences, one per line.
# Each sequence starts with the same 14 base pairs : these are from a sequencing adapter that should have been removed.

# This program trims the adapter sequences from each dna sequence in the input file, and saves them to a new file.
# Then, it prints the length of each adapter-free sequence to the screen.

# Open and read input file
inputfile = open("input.txt").readlines()
cleanseqs2 = open("Cleaned_sequences2.txt", "w")
count = 0 # initialize the count

# Process each line
for eachline in inputfile:
	count+=1
	eachline = eachline.strip()
	newline = eachline[14:] # Trim the first 14 bases
	newline_len = len(newline)
	cleanseqs2.write(newline + "\n") # Write the trimmed line to a file
	print(f"Length of line {count} is {newline_len}.") # Print the length information

# Close the files
cleanseqs2.close()
