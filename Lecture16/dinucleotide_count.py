#!/usr/bin/python3

# Lecture 16: A program to count the dinucleotides in a sequence
# Using a list to store all dinucleotides to be looked for in an input sequence
# INPUT
dna = "ATCGTATCGATGTACGCTGA"
dinucleotides = ['AA','AT','AG','AC',
                 'TA','TT','TG','TC',
                 'GA','GT','GG','GC',
                 'CA','CT','CG','CC']
# Set up a list to hold all the counts of each dinucleotide
all_counts = []

# PROCESS with a for loop
for dinucleotide in dinucleotides:
    count = dna.upper().count(dinucleotide)
    all_counts.append(count)

# OUTPUT
print(all_counts)
