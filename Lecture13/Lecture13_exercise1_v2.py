#!/usr/bin/python3

# Lecture 13, Exercise 1: Processing DNA in a file
# Written by Grace Newman (s2823303) on 31 October 2025
# Adapted from Al's Solution

# The file input.txt contains a number of DNA sequences, one per line.
# Each sequence starts with the same 14 base pairs : these are from a sequencing adapter that should have been removed.

# This program trims the adapter sequences from each dna sequence in the input file, and saves them to a new file.
# Then, it prints the length of each adapter-free sequence to the screen.

input_txt_contents = open('input.txt').read().upper().replace('ATTCGATTATAAGC','').split()

with open('Cleaned_sequences3.txt','w') as cleanseqs_w :
	for cleanones in input_txt_contents :
		cleanseqs_w.write(cleanones + '\n')
		cleanones
