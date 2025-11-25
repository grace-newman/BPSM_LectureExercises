#!/usr/bin/python3

# Lecture 19: Repeating Dinucleotides Example

import os, sys, re, subprocess
import matplotlib.pyplot as plt
import numpy as np

# Open the file, read it, and remove the newlines to get one long string
# then take the first 100000 characters
ecoli = open("/localdisk/data/BPSM/Lecture19/ecoli.txt").read().replace('\n', '').upper()[0:100000]

# Set sliding window size
window = 1000

# Initialize four lists to hold the numbers of each base
aa = []
tt = []
gg = []
cc = []

# Iterate over all the starting positions
counter =0
for start in range(len(ecoli) - window):
    # Get the current sliding window
    counter += 1
    print(counter)
    win = ecoli[start:start+window]
    # Count each of the four bases and append to the list
    aa.append(win.count('AA') / win.count('A'))
    tt.append(win.count('TT') / win.count('T'))
    gg.append(win.count('GG') / win.count('G'))
    cc.append(win.count('CC') / win.count('C'))
    

# Plot the lists with appropriate labels
plt.figure(figsize=(20,10))

# First panel
plt.subplot(221)
plt.plot(aa, label="AA rep")
plt.ylabel('Overrepresentation')
plt.xlabel('Position on genome')
plt.legend()

# Second panel
plt.subplot(222)
plt.plot(tt, label="TT rep")
plt.ylabel('Overrepresentation')
plt.xlabel('Position on genome')
plt.legend()

# Third panel
plt.subplot(223)
plt.plot(gg, label="GG rep")
plt.ylabel('Overrepresentation')
plt.xlabel('Position on genome')
plt.legend()

# Fourth panel
plt.subplot(224)
plt.plot(cc, label="CC rep")
plt.ylabel('Overrepresentation')
plt.xlabel('Position on genome')
plt.legend()

# Save and show
plt.savefig("Chart_16.png",transparent=True)
plt.show(block=False)
