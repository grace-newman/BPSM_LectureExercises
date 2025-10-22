#!/user/bin/python

# Exercise 1: Calculating A+T Content

# Program to calculate A+T content of a DNA sequence
# Written by Grace Newman (s2823303) on 22 Oct 2025

my_dna = 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'
A_count = my_dna.count('A')
T_count = my_dna.count('T')
AT_count = A_count + T_count
AT_content = AT_count/len(my_dna)
AT_percent = 100*AT_content
print("The A+T content of my short DNA fragment is " + str(int(AT_percent)) +"%")
