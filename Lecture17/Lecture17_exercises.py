#!/playtime/bin/python

# Lecture 17: Python 07 Pandas
# All lecture 17 exercises are in this one script
# Written by Grace Newman on 21 November 2025

# Use a pandas dataframe to address the following questions:
# - how many fungal species have genomes bigger than 100Mb? What are their names?
# - how many of each Kingdom/group (plants, animals, fungi and protists) have been sequenced?
# - which Heliconius species genomes have been sequenced?
# - which sequencing centre has sequenced the most plant genomes? the most insect genomes?
# - add a column giving the number of proteins per gene. Which genomes have at least 10% more proteins than genes?

# Import modules
import os, sys, re
import numpy as np
import pandas as pd
import string
# Get the file
os.system("wget -qO eukaryotes.tsv 'ftp://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/eukaryotes.txt'")

# Read in the file
df = pd.read_csv('eukaryotes.tsv',sep="\t")

# Question 1
print("Fungal species with genomes larger than 100Mb:\t")
print(df[df.apply(lambda x : x['Size (Mb)'] > 100 and x['Group'] in ['Fungi'], axis=1 )].shape[0])
# or
print(len(df[(df['Group'] == 'Fungi') & (df['Size (Mb)'] > 100) ]))
print("What are their names:\t")
print(set(df[df.apply(lambda x : x['Size (Mb)'] > 100 and x['Group'] in ['Fungi'], axis=1 )]["#Organism/Name"]))

# Question 2
print("How many of each Kingdom/Group have been sequenced?")
print(df["Group"].value_counts())

# Count unique ones (Credit Al's solution)
for Group in ['Plants', 'Animals', 'Fungi', 'Protists']:
    count = len(df[df['Group'] == Group])
# To count unique ones, we could get the names and turn them into a set
    count_unique = len(set(df[df['Group'] == Group]['#Organism/Name']))
# OR we could use the drop_duplicates method which may be clearer to read
    count_unique = len(df[df['Group'] == Group].drop_duplicates('#Organism/Name'))
    print("{} genomes for {} ({} unique)".format(count, Group, count_unique))

# Question 3
print("Which Heliconius species genomes have been sequenced?")
# credit Al's solution
hel = df[df.apply(lambda x : x['#Organism/Name'].startswith('Heliconius'), axis=1)]
print(hel)
print(hel[ ['#Organism/Name', 'Scaffolds'] ])

# Question 4
print("Which sequencing center has sequenced the most plant genomes?")
# "Plants" in set(df["Group"]) # True
print(df[df["Group"] == "Plants"]["Center"].value_counts()[0:1])

print("Which sequncing ceter has sequenced the most insect genomes?")
# "Insects" in set(df["SubGroup"]) # True
print(df[df["SubGroup"] == "Insects"]["Center"].value_counts().head(1))

# Question 5 # NOT WORKING
# Add a column giving the number of proteins per gene
# df['Proteins per gene'] = df['Proteins'] / df['Genes']

# print("Which genomes have at least 10% more proteins than genes?")
# credit Al's solution
# df[df['Proteins per gene'] >= 1.1][ ['#Organism/Name', 'Genes','Proteins','Proteins per gene'] ]
