#!/usr/bin/python3

# Programme/script to count dinucleotides in a sequence
# In this version, we remove the kmer counts that are zero, but only storing counts that are greater than zero

# INPUT
dna = "AATGATCGATCGTACGCTGA"
nonzero_counts = {}
dinucleotides = ['AA','AT','AG','AC', 
                 'TA','TT','TG','TC', 
                 'GA','GT','GG','GC', 
                 'CA','CT','CG','CC'] 
# PROCESS
# Loop through each element of the dinucleotides list and
# put the counts into the dict as a new key/value pair
# IF there are any
for dinucleotide in dinucleotides:        
    howmany = dna.upper().count(dinucleotide)
    if howmany > 0:
        nonzero_counts[dinucleotide] = howmany
