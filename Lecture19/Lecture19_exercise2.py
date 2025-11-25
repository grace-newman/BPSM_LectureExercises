#!/usr/bin/python3

# Lecture 19: Python Charting
# Exercise 2
# Written by Grace Newman on 25 November 2025

import os, sys, re, subprocess
import matplotlib.pyplot as plt
import numpy as np

# Using the working code from the Exercise 1, write a script that calls a function that you have written to do the processing.
# The default sequence should be the ecoli one we used for the lecture. The user should be able to provide the window size,
# whether they want AT content or GC content plotted, and what portion (base range) of the genome they want analysed


# Planning
# This script should call a function using input arguments defined by the user
# Inputs: at vs gc content, window size, portion of the genome to test
# Processing steps will involve getting the e coli genome, getting the at or gc content over the sliding windows, plotting
# Outputs: a graph
# Other things that should be added: more user interaction for things like graph coloring or other aesthetic preferences, there should be more error traps for the inputs.
# Right now the user must type AT or GC exactly, which is not ideal. II would also reduce the computeing power needed for calling the function by only actually calculating the 
# base conent type that was requested.


def content(base_type='AT', window=1000, genome_start=0, genome_end=10000) :
    # Open the file, read it, and remove the newlines to get one long string
    # then take the portion specified int he function call
    ecoli = open("/localdisk/data/BPSM/Lecture19/ecoli.txt").read().replace('\n', '').upper()[genome_start:genome_end]
    # Initialize a list for the AT content
    at_content = []
    gc_content = []
    # iterate over all the starting positions
    for start in range(len(ecoli) - window):
        # get the current sliding window
        win = ecoli[start:start+window]
        # count the a and t bases, divide by the window size and append to the list
        at_content.append(len(re.findall(r'[AT]', win))/ window)
        gc_content.append(len(re.findall(r'[GC]', win))/ window)
    if base_type == 'AT' :
        # Plot the lists with appropriate labels
        plt.figure(figsize=(20,10))
        plt.plot(at_content, label="AT Content")
        plt.ylabel('AT Content')
        plt.xlabel('Position on genome')
        plt.legend()
    elif base_type == 'GC':
        plt.figure(figsize=(20,10))
        plt.plot(gc_content, label="GC Content")
        plt.ylabel('GC Content')
        plt.xlabel('Position on genome')
        plt.legend()
    # Save and show
    plt.savefig("exercise2plot.png",transparent=True)
    plt.show(block=False)

# Ask user for input arguments:
my_type = input("AT or GC content?\t")
my_window = int(input("Window size:\t"))
my_genome_start = int(input("Genome start position:\t"))
my_genome_end = int(input("Genome end position:\t"))

# Call the function
content(base_type = my_type, window = my_window, genome_start = my_genome_start, genome_end= my_genome_end) 
