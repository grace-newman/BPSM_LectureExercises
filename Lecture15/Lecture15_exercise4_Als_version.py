#!/usr/bin/python3

# Write a FUNCTION that, given any DNA sequence, will print
# all the k-mers (of a chosen size e.g. 4-mers) that occur more than some
# chosen number of times.
# Written by Al on 04 Nov 25
# --------------------------------------------------------------

# Set some sensible defaults for the function
def find_my_kmers(dna,ksize=2,min_kfreq=3) :
# Error traps for inappropriate values, what to put
   if ksize > len(dna) :
     return "Sorry, your kmer length is longer than your DNA (" + str(len(dna)) +" bases)." 
   if ksize < 2 or ksize > 50 :
     return "Sorry, inappropriate kmer length, only 2 to 50 accepted here."
   print("Processing sequence of length",len(dna),"for kmers longer than",ksize,"and frequency greater than",min_kfreq)
   kmersfound = []
   kmerstarts = list(range(0,len(dna)))
   for base in kmerstarts:
       if (base+ksize) < len(dna)+1:
           seqout = (dna)[base:base+ksize]
           kmersfound = kmersfound + [seqout] 
   nrset = list(set(kmersfound)) 
# Maybe use a list for the multiple returned values?

   returnstuff = []
   for kfreqfind in nrset:
       if kmersfound.count(kfreqfind) > min_kfreq :
           returnstuff.append(kfreqfind.upper()+": "+str(kmersfound.count(kfreqfind)))
   return print(returnstuff)
