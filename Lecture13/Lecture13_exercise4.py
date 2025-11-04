#!/usr/bin/python3

# This code has not been tested. Need to review Al's solution.

# Lecture 13, Exercise 4: Size-binning DNA sequences
# Written by Grace Newman (s2823303) on 3 November 2025
# Adapted from Al's solution code

# A python script which creates nine new 'size range' directories, one for sequences between 100 and 199 bases long, one for sequences between 200 and 299 bases long etc.
# Use a .dna file as inpur ad write out each DNA sequeence in that input file to a separate file in the appropriate 'size range' directory.

import os, sys, subprocess, shutil

for file_name in os.listdir('dna_files/') : 
    if file_name.endswith('.dna') : 
        f'Reading sequences from {file_name}'
        dna_file = open('dna_files/' + file_name)
# This loop then looks at each line and gets the length
# Note the indentation...
        for line in dna_file : 
            dna = line.rstrip('\n') 
            length = len(dna) 
            print(f'\tFound a DNA sequence with length {str(length)}' )

for file_name in  sorted(os.listdir('dna_files')) : 
# Check if the file name ends with .dna
  if file_name.endswith('.dna') : 
    print('Reading sequences from ' + file_name) 
# Open the file and process each line
    dna_file = open('dna_files/' + file_name) 
# Calculate the sequence length 
    for line in dna_file :
      dna = line.rstrip('\n') 
      length = len(dna) 
      print('\tsequence length is ' + str(length)) 
# Go through each size bin and check if the sequence belongs in it
      for bin_lower in list(range(100,1000,100)) : 
        bin_upper = bin_lower + 99 
        if length >= bin_lower and length <= bin_upper : 
          print('\t\tbin is ' + str(bin_lower) + ' to ' + str(bin_upper)) 

for bin_lower in list(range(100,1000,100)) :
	bin_upper = bin_lower + 99
	bin_directory_name = str(bin_lower) + '_' + str(bin_upper)
	shutil.rmtree(bin_directory_name)
	os.mkdir(bin_directory_name)

seq_number = 1
for file_name in os.listdir('dna_files') : 
# Check if the file name ends with .dna
  if file_name.endswith('.dna') : 
    print('Reading sequences from ' + file_name) 
# Open the file and process each line
    dna_file = open('dna_files/' + file_name) 
    for line in dna_file :
# Calculate the sequence length 
      dna = line.rstrip('\n') 
      length = len(dna) 
      print('\tsequence length is ' + str(length))
# Go through each size bin and check if the sequence belongs in it
      for bin_lower in list(range(100,1000,100)) : 
        bin_upper = bin_lower + 99 
        if length >= bin_lower and length <= bin_upper : 
          print('\t\tbin is ' + str(bin_lower) + ' to ' + str(bin_upper)) 
          bin_directory_name = str(bin_lower) + '_' + str(bin_upper) 
          output_path = bin_directory_name + '/' + str(seq_number) + '.dna' 
          output = open(output_path, 'w') 
          output.write(dna) 
          output.close() 
# Increment the sequence number
          seq_number = seq_number+1
