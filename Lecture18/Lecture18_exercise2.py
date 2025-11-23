#!/usr/bin/python3

# Lecture 18 Regular Expressions
# Exercise 2: DNA Sequence Double Digest
# Written by Grace Newman on 23 November 2025
# Adapted from Al's solution code

# A file called long_dna.txt has been put in the following directory:
# /localdisk/data/BPSM/Lecture18

# It contains a made-up DNA sequence.
# What fragment lengths will we get if we digest the sequence with a novel restriction enzyme BpsmI, whose recognition site is ANT*AAT, where * indicates the position of the cut site.
# What will the fragment lengths be if we do a double digest with both BpsmI and BpsmII (whose recognition site is GCRW*TG)?
# What are the sequences of the fragments themselves?

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import re

BpsmI='A[GATC]TAAT'
BpsmII='GC[AG][AT]TG'

# Open and read in the file
dna = open('/localdisk/data/BPSM/Lecture18/long_dna.txt').read().rstrip('\n') 
last_cut = 0
findnum=0
for matching in re.finditer(BpsmI, dna):
    findnum += 1
    cut_position = matching.start() + 3
# Distance from the current cut site to the previous one
    fragment_size = cut_position - last_cut
    print('Fragment size is ' + str(fragment_size))
    last_cut = cut_position
# We also have to remember the last fragment, from the last cut to the end:
    if findnum == len(list(re.finditer(BpsmI, dna))) :
       fragment_size = len(dna) - last_cut
       print('Fragment size is ' + str(fragment_size))

# Double digest
# First, define both enzymes sites
BpsmI='A[GATC]TAAT'
BpsmII='GC[AG][AT]TG'

# Make a list to store the cut positions for both enzymes
all_cuts = []
# Add cut positions for BpsmI
for match in re.finditer(BpsmI, dna): 
    all_cuts.append(match.start() + 3) 

# Add cut positions for BpsmII
for match in re.finditer(BpsmII, dna): 
    all_cuts.append(match.start() + 4)

print(all_cuts)
# These aren't in sequential order, so just sort them
all_cuts.sort()
all_cuts

# Double digest run
last_cut = 0
counter = 0
for cut_position in all_cuts:
    counter +=1
    fragment_size = cut_position - last_cut
    print('Fragment '+str(counter)+' size is ' + \
       str(fragment_size) +': '+ str(last_cut)+ ' to ' +str(cut_position) )
    last_cut = cut_position

# Now the last fragment
fragment_size = len(dna) - last_cut
counter +=1
print('Fragment '+str(counter)+' size is ' + \
  str(fragment_size) +': '+ str(last_cut)+ ' to ' +str(len(dna)) )

# Sequences themselves:
# We have just worked out where the enzymes cut the DNA sequence,
# so all we need to do is to use the cut positions as index positions to
# substring the dna sequence string!

# Let's use a dictionary to store the fragment sequences
fragment_sequences = {}
# Double digest run
last_cut = 0
counter = 0
for cut_position in all_cuts:
    counter +=1
    fragment_size = cut_position - last_cut
    print('Fragment '+str(counter)+' size is ' + \
       str(fragment_size) +': '+ str(last_cut)+ ' to ' +str(cut_position) )

# Get the sequence substring
    fragment_sequences['Fragment'+str(counter)] = dna[last_cut:cut_position]
    print(fragment_sequences['Fragment'+str(counter)])
# Get the fragment start and end
    fragends = dna[last_cut:cut_position][0:6] + '...' + dna[last_cut:cut_position][-6:]
    print('Fragment '+str(counter)+ ' has ends: '+fragends+'\n')
    last_cut = cut_position
# Now the last fragment
fragment_size = len(dna) - last_cut
counter +=1
print('Fragment '+str(counter)+' size is ' + \
  str(fragment_size) +': '+ str(last_cut)+ ' to ' +str(len(dna)) )
fragment_sequences['Fragment'+str(counter)] = dna[last_cut:]
print(fragment_sequences['Fragment'+str(counter)])
fragends = dna[last_cut:][0:6] + '...' + dna[last_cut:][-6:]
print('Fragment has ends: '+fragends)

# Show all the sequences
print(('\n########\n').join(list(fragment_sequences.values())))
