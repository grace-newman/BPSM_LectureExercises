#!/usr/bin/python3

# Lecture 15, Exercise 3: Base counter
# Wrtten by Grace Newman (s2823303) on 6 November 2025

# A Python function that will take a DNA sequence along with an optional threshold and return True or False to indicate whether
# the DNA sequence contains a high proportion of undetermined bases (i.e not A, T, G or C).

def undetermined_base_percent(dna_seq, threshold_percent=20):
    length = len(dna_seq)
    count = 0
    for base in dna_seq.upper():
        if base.upper() not in ['A','T','G','C']:
	    count+=1
    undetermined_percent = (100*count)/length
    return undetermined_percent >= threshold_percent
