#!/usr/bin/python3

# Lecture 19: Sliding Window Plot Example

import os, sys, re, subprocess
import matplotlib.pyplot as plt
import numpy as np

# Open the file, read it, and remove the newlines to get one long string
# then take the first 100000 characters
ecoli = open("/localdisk/data/BPSM/Lecture19/ecoli.txt").read().replace('\n', '').upper()[0:100000]

# Set sliding window size
window = 1000

# Initialize four lists to hold the numbers of each base
a = []
t = []
g = []
c = []

# iterate over all the starting positions
for start in range(len(ecoli) - window):
    # get the current sliding window
    win = ecoli[start:start+window]
    # count each of the four bases and append to the list
    a.append(win.count('A') / window)
    t.append(win.count('T') / window)
    g.append(win.count('G') / window)
    c.append(win.count('C') / window)

# Plot the lists with appropriate labels
plt.figure(figsize=(20,10))
plt.plot(a, label="A")
plt.plot(t, label="T")
plt.plot(g, label="G")
plt.plot(c, label="C")
plt.ylabel('Fraction of bases')
plt.xlabel('Position on genome')
plt.legend()

# Save and show
plt.savefig("Chart_15.png",transparent=True)
plt.show(block=False)
