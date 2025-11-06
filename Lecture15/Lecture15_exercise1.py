#!/usr/bin/python3

# Lecture 15, Exercise 1: Amino acid percentages, part 1
# Written by Grace Newman (s2823303) on 6 November 2025

# A function that takes two arguments (a protein sequence and an amino acid residue code) and returns the percentage of the protein that the amino acid makes up.

def aa_percent(protein_seq, aa_residue):
    length = len(protein_seq)
    aa_count = protein_seq.upper().count(aa_residue.upper())
    aa_percentage = (100*aa_count)/length
    return aa_percentage
