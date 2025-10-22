#!/usr/bin/python

# Exercise 2: Complementing DNA

# A program that will print the complement of a DNA sequence
# Written by Grace Newman (s2823303) on 22 October 2025

my_dna = 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'
A_to_X = my_dna.replace('A','X') # replace A with a placeholder X
T_to_A = A_to_X.replace('T','A') # replace all T's with their complement A's
X_to_T = T_to_A.replace('X','T') # replace X's with T's
G_to_Y = X_to_T.replace('G','Y') # replace G with a placeholder Y
C_to_G = G_to_Y.replace('C','G') # replace all C's with complement G's
Y_to_C = C_to_G.replace('Y','C') # replace Y's with C's
print("My DNA sequence:\t" + my_dna)
print("My DNA complement:\t" + Y_to_C)
