#!/usr/bin/python3

# Lecture 16, Exercise 2: DNA translation
# Written by Grace Newman (s2823303) on 20 November 2025
# A Python program that will take any DNA sequence and translate it into protein using the translation table.
# Generate a translation in all three forward frames and all three reverse frames.

# Here is a dict theat stores a codon usage table for translation:
gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

# A function to split the dna sequence into codons
# pass the reading frame as an argument
def translate_dna(dna, rf=1):
    dna = dna.upper()
    if rf not in [-3,-2,-1,1,2,3]:
	print("Not a valid reading frame. Choose a reading frame from the following: -3, -2, -1, 1, 2, 3")
        return
    if rf in [-3,-2,-1] :
        # Make the reverse complement
        c_dna = dna.replace("G","c").replace("A","t").replace("T","a").replace("C","g").upper() # make the complement strand
        rc_dna = c_dna[::-1] # reverse the string using a slice
        dna = rc_dna
    # Translate...
    protein = "" # initialize a string for the amino acids
    # Use the sliding window method from lecture 13, exercise 3, to append each kmer to a list
    for i in list(range(abs(rf)-1,len(dna)-2,3)): # note that we are using the absolute value of the rf
        codon = dna[i:3+i]
        # Use the dict to translate each codon to an amino acid
        aa = gencode.get(codon,"X") # if there is an unknown base in a codon and there's no key, it will add an X to the protein sequence
        protein = protein + aa
    return protein
