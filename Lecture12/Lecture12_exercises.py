#!/usr/bin/python3

# Exercise 4: Make Some FASTA Files

# A program that splits a genomic DNA sequence in the text file plain_genomic_seq.txt into separate files of coding and non-coding sections.
# Written by Grace Newman on 24 OCtober 2025

import os, subprocess, shutil

# Copy the local file to your current directory and store the local sequence in a variable
os.system("cp /localdisk/data/BPSM/Lecture12/plain_genomic_seq.txt   . ")
local_seq = open("plain_genomic_seq.txt").read().upper().rstrip() # convert to uppercase and remove empty ending lines
local_seq_singleline = local_seq.replace("\n","") # convert to a single line
len(local_seq_singleline)

# Look for then remove non-DNA characters from local file
local_seq_singleline_anythingleft = local_seq_singleline.replace("G","").replace("A","").replace("T","").replace("C","")
local_seq_singleline_anythingleft
local_seq_singleline_reallyDNA = local_seq_singleline.replace("X","").replace("S","").replace("K","").replace("L","")
local_seq_singleline_reallyDNA
local_seq_singleline_ready = local_seq_singleline_reallyDNA # make a copy for later
# Alternatively,  use the set command to show you all the unique characters in the file
# set(list(local_seq.rstrip()))

# Split the local file into coding and non-coding sections
local_exon01 = local_seq_singleline_ready[0:63]
local_intron01 = local_seq_singleline_ready[63:90]
local_exon02 = local_seq_singleline_ready[90:]

# Write out the local files
local_exon01_out = open("local_exon01.fasta", "w")
local_exon01_out.write(">LocalSeq_exon01_length" + str(len(local_exon01)) + "\n")
local_exon01_out.write(local_exon01)
local_exon01_out.close()

local_intron01_out = open("local_intron01.fasta", "w")
local_intron01_out.write(">LocalSeq_intron01_length" + str(len(local_intron01)) + "\n")
local_intron01_out.write(local_intron01)
local_intron01_out.close()

local_exon02_out = open("local_exon02.fasta", "w")
local_exon02_out.write(">LocalSeq_exon02_length" + str(len(local_exon02)) + "\n")
local_exon02_out.write(local_exon02)
local_exon02_out.close()


# Aquire the remote file and save locally
subprocess.call("esearch -db nucleotide -query \"AJ223353[accession]\" | efetch -format fasta | grep -v \">\" > AJ223353_noheader.fasta3", shell=True)
remotefile = open("AJ223353_noheader.fasta3").read().upper() # convert to uppercase
remotefile_singleline = remotefile.replace("\n","") # convert to a single line
remotefile_singleline_ready = remotefile_singleline # make a copy for later use
len(remotefile_singleline_ready)

# Remove non-nucleotide characters from the remote file
remotefile_singleline_anythingleft = remotefile_singleline.replace("G","").replace("A","").replace("T","").replace("C","")
remotefile_singleline_anythingleft # there are none

# Split the remote sequence into coding and non-coding sections
remote_noncoding01 = remotefile_singleline_ready[0:28]
remote_exon01 = remotefile_singleline_ready[28:409]
remote_noncoding02 = remotefile_singleline_ready[409:]

# Write out the remote files
remote_noncoding01_out = open("remote_noncoding01.fasta", "w")
remote_noncoding01_out.write(">AJ223353_noncoding01_length" + str(len(remote_noncoding01)) + "\n")
remote_noncoding01_out.write(remote_noncoding01)
remote_noncoding01_out.close()

remote_exon01_out = open("remote_exon01.fasta", "w")
remote_exon01_out.write(">AJ223353_exon01_length" + str(len(remote_exon01)) + "\n")
remote_exon01_out.write(remote_exon01)
remote_exon01_out.close()

remote_noncoding02_out = open("remote_noncoding02.fasta", "w")
remote_noncoding02_out.write(">AJ223353_noncoding02_length" + str(len(remote_noncoding02)) + "\n")
remote_noncoding02_out.write(remote_noncoding02)
remote_noncoding02_out.close()

# Write the combined files for coding and non-coding sequences

# Coding Regions:
exons_out = open("All_exons.fasta", "w")
exons_out.write(">AJ223353_exon01_length" + str(len(remote_exon01)) + "\n" + remote_exon01 + "\n")
exons_out.write(">LocalSeq_exon01_length" + str(len(local_exon01)) + "\n" + local_exon01 + "\n")
exons_out.write(">LocalSeq_exon02_length" + str(len(local_exon02)) + "\n" + local_exon02)
exons_out.close()
print(open("All_exons.fasta").read())

# Non-coding Regions:
introns_out = open("All_noncodings.fasta", "w")
introns_out.write(">AJ223353_noncoding01_length" + str(len(remote_noncoding01)) + "\n" + remote_noncoding01 + "\n")
introns_out.write(">AJ223353_noncoding02_length" + str(len(remote_noncoding02)) + "\n" + remote_noncoding02 + "\n")
introns_out.write(">LocalSeq_intron01_length" + str(len(local_intron01)) + "\n" + local_intron01)
introns_out.close()
print(open("All_noncodings.fasta").read())
