#!/usr/bin/python3

# Lecture 16

# Programme/script to count dinucleotides in a sequence
# Using a list to store all dinucleotides to be looked for in a new input sequence
# INPUT
dna = "AATGATGAACGAC"
dinucleotides=[]
for first in 'ATGC' :
  for second in 'ATGC' :
    dinucleotides.append(str(first)+str(second))

dinucleotides
['AA', 'AT', 'AG', 'AC', 'TA', 'TT', 'TG', 'TC', 'GA', 'GT', 'GG', 'GC', 'CA', 'CT', 'CG', 'CC'] # a list of all possible dinucleotides

# Set up an empty dict to hold all the counts of each dinucleotide
all_counts = {}

# PROCESS
# Loop through each element of the dinucleotides list and
# put the counts into the dict as a new key/value pair
for dinucleotide in dinucleotides: 
    count = dna.upper().count(dinucleotide) 
    print("count is " + str(count) + " for " + dinucleotide) 
    all_counts[dinucleotide] = count
