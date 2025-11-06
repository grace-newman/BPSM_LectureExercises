#!/usr/bin/python3

# Lecture 15, Exercise 2: Amino acid percentages, part 2
# Written by Grace Newman (s2823303) on 6 November 2025

# A function that takes two arguments (a protein sequence and an amino acid residue code) and returns the percentage of the protein that the amino acid makes up.
# Modify the function from the previous exercise above so that it accepts a list of amino acid residues rather than a single one, and count these within the protein sequence.
# If no list is given, the function should return the percentage of hydrophobic amino acid residues (i.e. amino acids A, I, L, M, F, W, Y, V).

def aa_percent_v2(protein_seq, aa_list=['A','I','L','M','F','W','Y','V']):
    length = len(protein_seq)
    aa_count = 0
    for residue in aa_list:
        aa_count = aa_count + protein_seq.upper().count(residue.upper())
    aa_percentage = (100*aa_count)/length
    return aa_percentage
