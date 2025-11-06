#!/usr/bin/python3

# Lecture 15, Exercise 5: Kmer counting again
# Written by Grace Newman (s2823303) on 6 November 2025

# A script that, given any DNA sequence, will print the k-mers (e.g. 4-mers) that occur more than some number of times n.

# Import modules
import sys

# Define the function
def kmer_count(dna_seq, kmersize, minfrequency):
    dna_seq = dna_seq.upper()
    kmer_list = [] # list for all the kmers
    kmers_n = [] # list for kmers that appear more than the min frequency
    # Use the sliding window method from lecture 13, exercise 3, to append each kmer to a list
    for i in list(range(0,len(dna_seq),1)):
        kmer_list.append(dna_seq[i:kmersize+i])
    # Count the occurences of the kmers
    for kmer in kmer_list:
        if kmer_list.count(kmer) > minfrequency:
            kmers_n.append(kmer) # a list of all the k_mers that occur more than the min frequency
    return set(kmers_n)

# Ask the user for the input values
dna = input("Enter the DNA sequence:\t") # I could add a lot more conditionals and error traps for the input dna sequence.
kmersz = int(input("Enter the kmer size:\t"))
minfreq = int(input("Enter the threshold number (kmers that occur more than this number of times):\t"))

# Call the function
result = kmer_count(dna, kmersz, minfreq)
print(result)
