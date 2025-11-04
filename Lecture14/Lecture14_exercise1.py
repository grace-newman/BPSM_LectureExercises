#!/usr/bin/python3

# Lecture 14, Exercise 1: Processing tabular data
# Written by Grace Newman (s2823303) on 4 November 2025

# Print out the gene names for all genes from the species Drosophila melanogaster or Drosophila simulans.
# Print out the gene names for all genes that are between 90 and 110 bases long.
# Print out the gene names for all genes whose AT content is less than 0.5 and whose expression level is greater than 200.
# Print out the gene names for all genes whose name begins with "k" or "h" except those belonging to Drosophila melanogaster.
# For each gene, print out a message giving the gene name and saying whether its AT content is high (greater than 0.65), low (less than 0.45) or medium (between 0.45 and 0.65).


# Read in the data
fly_data = open("data.csv").readlines()

print("\nGene names for all genes from species Drosophila melanogaster or Drosophila simulans...")
for line in fly_data:
    fly_line = line.rstrip().split(",") # change each row of data from a string into a list
    if fly_line[0] == "Drosophila melanogaster" or fly_line[0] == "Drosophila simulans" :
        print("Gene name:", fly_line[2], "\tSpecies:", fly_line[0])

print("\nGene names for all genes that are between 90 and 110 bases long...")
for line in fly_data:
    fly_line = line.rstrip().split(",") # change each row of data from a string into a list
    if (len(fly_line[1]) > 90 and len(fly_line[1]) < 110):
        print("Gene name:", fly_line[2], "\tSequence Length:", len(fly_line[1]))

print("\nGene names for all genes whose AT content is less than 0.5 and whose expression level is greater than 200...")
for line in fly_data:
    fly_line = line.rstrip().split(",") # change each row of data from a string into a list
    if (fly_line[1].upper().count("A") + fly_line[1].upper().count("T"))/len(fly_line[1]) < 0.5 and int(fly_line[3]) > 200:
        print("Gene name:", fly_line[2], "\tAT Content: ", round((fly_line[1].upper().count("A") + fly_line[1].upper().count("T"))/len(fly_line[1]), 4), "\tExpression: ", fly_line[3])

print("\nGene names for all genes whose name begins with \"k\" or \"h\" except those belonging to Drosophila melanogaster...")
for line in fly_data:
    fly_line = line.rstrip().split(",")
    if (fly_line[2].startswith("k") or fly_line[2].startswith("h")) and fly_line[0] != "Drosophila melanogaster" :
        print("Gene name:", fly_line[2], "\tSpecies:", fly_line[0])

print("\nAT Content...")
for line in fly_data:
    fly_line = line.rstrip().split(",")
    if (fly_line[1].upper().count("A") + fly_line[1].upper().count("T"))/len(fly_line[1]) > 0.65 :
        print("Gene name:", fly_line[2], "\tAT Content: ", round((fly_line[1].upper().count("A") + fly_line[1].upper().count("T"))/len(fly_line[1]), 4), "\tHigh")
    elif (fly_line[1].upper().count("A") + fly_line[1].upper().count("T"))/len(fly_line[1]) >= 0.45 and (fly_line[1].upper().count("A") + fly_line[1].upper().count("T"))/len(fly_line[1]) <= 0.65 :
        print("Gene name:", fly_line[2], "\tAT Content: ", round((fly_line[1].upper().count("A") + fly_line[1].upper().count("T"))/len(fly_line[1]), 4), "\tMedium")
    elif (fly_line[1].upper().count("A") + fly_line[1].upper().count("T"))/len(fly_line[1]) < 0.45 :
        print("Gene name:", fly_line[2], "\tAT Content: ", round((fly_line[1].upper().count("A") + fly_line[1].upper().count("T"))/len(fly_line[1]), 4), "\tLow")
    else:
        print("Something is wrong")

print("\nAll done!")
