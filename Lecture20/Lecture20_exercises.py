#!/usr/bin/python3

# Lecture 20: Biopython
# Written by Grace Newman on 06 December 2025

# Import the required modules
from Bio import Entrez, SeqIO
import os, subprocess
Entrez.email="G.E.Newman@sms.ed.ac.uk"
Entrez.api_key=subprocess.check_output("echo ${NCBI_API_KEY}", shell=True).rstrip().decode()

# Exercise 1: How many complete COX1 protein records are there for mammals?

# Define and do the search:
result = Entrez.read(Entrez.esearch(db="protein", term="Mammalia COX1 complete", retmax="20"))

# Extract info from the results of the search
print("Number of complete protein records for mammalian COX1 proteins:", result["Count"])


# Exercise 2: What is the average length of the protein sequences?
prot_count = 0
prot_length_total = 0
for accession in result['IdList']:
    gb_file = Entrez.efetch(db="protein",id=accession, rettype="gb")
    record = SeqIO.read(gb_file, "genbank")
    prot_count = prot_count + 1
    prot_length = len(record.seq)
    prot_length_total = prot_length_total + prot_length
    mean_length = int(prot_length_total/prot_count)
print("The average length of a mammalian COX1 complete protein sequence is ", mean_length, "amino acids.")
# Exercise 3
# Write a function that will answer the question for any gene name and any taxonomic group.
search_results = []
def get_average_length(taxonomy, gene, howmany=10):
    from Bio import Entrez, SeqIO
    import os, subprocess
    Entrez.email = "s123456@ed.ac.uk"
    Entrez.api_key=subprocess.check_output("echo ${NCBI_API_KEY}", shell=True).rstrip().decode()
    search_term = taxonomy + " " + gene + " complete"
    search_output = open(search_term.replace(" ","_")+"_outputs.txt","w")
    mysearch = Entrez.esearch(db="protein", term=search_term, retmax=howmany)
    result = Entrez.read(mysearch)
    loopcounter = total_length = 0
    for accession in result['IdList']:
        loopcounter += 1
        gb_file = Entrez.efetch(db="protein",id=accession,rettype="gb")
        record = SeqIO.read(gb_file, "genbank")
        total_length =  total_length + len(record.seq)
        search_results.append([search_term,record.id,record.description,len(record.seq),record.seq])
    print(record.id+"\t"+record.description+"\t"+str(len(record.seq))+"\t"+record.seq[0:50]+"...")
    search_output.write(record.id+"\t"+record.description+"\t"+str(len(record.seq))+"\t"+str(record.seq)+"\n")
    mean_length = int(total_length/loopcounter)
    return print(("\nThe mean length was "+str(mean_length)+" amino acids.\n"))
    close(search_output)
