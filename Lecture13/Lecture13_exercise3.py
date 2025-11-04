#!/usr/bin/python3

# Note: currently, this file contains multiple sections that aren't meant to me run all at once.

# Lecture 13, Exercise 3: Sliding Windows
# by Grace Newman (s2823303) on 3 November 2025

# A program that will generate overlapping short segments from a long string.
# A program that generates segments that are 30 bases long, with a window offset of 3 using the protein coding region of the AJ223353 NCBI sequence.

# Read in the coding sequence from a file.
fasta_file = open("remote_exon01.fasta")
header = fasta_file.readline()
coding_sequence = fasta_file.readline()
print(header)
print("Coding Sequence: " + coding_sequence)

# a. Print each sliding window to the screen.
for i in list(range(0,(len(coding_sequence)-29),3)):
	print(coding_sequence[i:30+i])

# b. Print the GC content of each sliding window segment and of the full sequence.
GC_content_fullseq = (coding_sequence.count('G') + coding_sequence.count('C')) / len(coding_sequence)
f"GC content of the full sequence: {GC_content_fullseq}" 
count = 0
for i in list(range(0,(len(coding_sequence)-29),3)):
	count = count + 1
	segment = coding_sequence[i:30+i]
	GC_content_segment = (segment.count('G') + segment.count('C')) / len(segment)
	f"Segment {count}: {segment}"
	f"Segment {count} GC Content: {GC_content_segment}" 

# c. Write out the individual segments in fasta format into individual fasta files.
count = 0
for i in list(range(0,(len(coding_sequence)-29),3)):
	count = count + 1
	segment = coding_sequence[i:30+i]
	GC_content_segment = (segment.count('G') + segment.count('C')) / len(segment)
	with open(f"Lecture13_exercise3_segment_{count}.out.fasta","w") as segment_w :
		segment_w.write("> Segment " + str(count) + " | Length: " + str(len(segment)) + " | GC Content: " + str(round(GC_content_segment,5)) + "\n")
                segment_w.write(segment + "\n")

# d. Write out the individual segments in fasta format into a single file.

count = 0
with open("Lecture13_exercise3_segments.fasta","w") as segments_w :
	for i in list(range(0,(len(coding_sequence)-29),3)):
        	count = count + 1
        	segment = coding_sequence[i:30+i]
        	GC_content_segment = (segment.count('G') + segment.count('C')) / len(segment)
		segments_w.write("> Segment " + str(count) + " | Length: " + str(len(segment)) + " | GC Content: " + str(round(GC_content_segment,5)) + "\n")
		segments_w.write(segment + "\n")

# e. Modify your script to include the partial segments we get at the end.
GC_content_fullseq = (coding_sequence.count('G') + coding_sequence.count('C')) / len(coding_sequence)
f"GC content of the full sequence: {GC_content_fullseq}" 
count = 0
for i in list(range(0,len(coding_sequence),3)):
        count = count + 1
        segment = coding_sequence[i:30+i]
	segment_len = len(segment)
        GC_content_segment = (segment.count('G') + segment.count('C')) / len(segment)
        f"Segment {count}: {segment}"
        f"Segment {count} GC Content: {GC_content_segment} Segment Length: {segment_len}"
