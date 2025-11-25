#!/usr/bin/python3

# Lecture 19: Python Charting
# Exercise 1
# Written by Grace Newman on 25 November 2025

import os, sys, re, subprocess
import matplotlib.pyplot as plt
import numpy as np

# Open the file, read it, and remove the newlines to get one long string
# then take the first 100000 characters
ecoli = open("/localdisk/data/BPSM/Lecture19/ecoli.txt").read().replace('\n', '').upper()[0:]

# Set sliding window size
window = 1000

# Initialize a list for the AT content
at_content = []

# iterate over all the starting positions
for start in range(len(ecoli) - window):
    # get the current sliding window
    win = ecoli[start:start+window]
    # count the a and t bases, divide by the window size and append to the list
    at_content.append(len(re.findall(r'[AT]', win))/ window)

# Plot the lists with appropriate labels
plt.figure(figsize=(20,10))
plt.plot(at_content, label="AT Content")
plt.ylabel('AT Content')
plt.xlabel('Position on genome')
plt.legend()

# Save and show
plt.savefig("AT_content.png",transparent=True)
plt.show(block=False)
