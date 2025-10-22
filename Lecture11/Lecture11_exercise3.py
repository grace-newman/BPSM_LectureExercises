#!/usr/bin/python

# Exercise 3: Restriction fragment lengths

# A program that will calculate the size of the two fregments that will be produced with the DNA sequence is digested with EcoRI
# EcoRI is a restriction enzyme that cuts at the motif G*AATTC (the position of the cut is indicated by an asterisk)
# Written by Grace Newman (s2823303) on 22 October 2025

my_dna = 'ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT'
cut_position = my_dna.find('GAATTC')
fragment1 = my_dna[:(cut_position+1)]
fragment2 = my_dna[(cut_position+1):]
print("Size of fragment 1:\t" + str(len(fragment1)))
print("Size of fragment 2:\t" + str(len(fragment2)))
# print(str(len(my_dna))) # checking the length of the full sequence
