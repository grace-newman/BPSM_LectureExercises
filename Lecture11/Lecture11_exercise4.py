#!/usr/bin/python

# Exercise 4: Splicing Out Introns

# A program that prints just the coding region of a DNA sequence.
	# The given seqience comprises two exons and an intron. The first exon runs from the start of the sequence to the sixty-third real character,
	# and the second exon runs from the ninety-first real character to the end of the sequence.
# Written by Grace Newman (s2823303) on 22 October 2025

my_genomic_dna = 'ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT'
exon1 = my_genomic_dna[:63]
exon2 = my_genomic_dna[90:]
coding_dna = exon1 + exon2
print("Coding region:\t" + coding_dna)

# A program to calculate what percentage of the DNA sequence is coding.

coding_percent = 100 * (len(coding_dna)/len(my_genomic_dna))
print("Percent of DNA sequence that is coding:\t" + str(int(coding_percent)))

# A program that willprint out the original genomic DNA sequence with coding bases in uppercase and noncoding bases in lowercase.

intron = my_genomic_dna[63:89]
intron_lower = intron.lower()
print("Genomic DNA sequence:\t" + exon1 + intron_lower + exon2)
