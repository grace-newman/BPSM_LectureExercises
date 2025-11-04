#!/usr/bin/python3

# Look into Al's solution for alternate methods when review for the exam.

# Lecture 14, Exercise 2: K-mer counting
# Written by Grace Newman (s2823303) on 4 November 2025

# A program that, given any DNA sequence, will print all the k-mers (e.g. 4-mers) that occur more than some number of times n.

import sys

dna = str(input("Enter the DNA sequence:\t")) # I could add a lot more conditionals and error traps for the input dna sequence.
k = int(input("Enter the kmer size:\t"))
n = int(input("Enter the threshold number (kmers that occur more than n times):\t"))

#dna="ATGAGCATCATGGAGAGA"
#k=2 # kmer size
#n=2 # more than this number found

dna = dna.upper()

# Initialize an empty list for the k-mers
kmer_list = []
kmers_n = []

# Use the lsiding window method from lecture 13, exercise 3, to append each kmer to a list
for i in list(range(0,len(dna),1)):
    kmer_list.append(dna[i:k+i])

# Count the occurences of the kmers
for kmer in kmer_list:
    if kmer_list.count(kmer) > n :
        print(kmer)
