#!/usr/bin/python3

# Lecure 18: Regular Expressions
# Exercise 1: Accession Numbers
# Written by Grace Newman on 23 November 2025

# A python script that will print only the accession numbers that satisfy the following criteria individually

import re


accessions = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']

for i in accessions :
    # Contain the number 5
    if re.search(r'5', i) :
        print('Accession that contains the number 5:\t' + i)
    # Contain the letter d or e
    if re.search(r'd|e', i) :
        print('Accession that contains d or e:\t' + i)
    # Contain the letters de in that order, with any type or amount of characters between them
    if re.search(r'd.*e', i) :
        print("Accession that contains d and e in that order:\t" + i)
    # contain the letters d and e in that order with a single letter between them
    if re.search(r'd.e', i) :
        print("Accession that contains d and e, in that order, with any single letter between them:\t" + i)
    # contain both the letters d and e in any order
    if re.search(r'd', i) and re.search(r'e', i) :
        print("Accession that contains d and e in any order:\t" + i)
    # start with x or y
    if re.search(r'^[xy]', i) :
        print("Accession that starts with x or y:\t" + i)
    # start with x or y and end with e
    if re.search(r'^[xy]', i) and re.search(r'e$', i) :
        print("Accession that starts with x or y and ends with e:\t" + i)
    # contains any 3 numbers in any order
    if len(re.findall(r'\d', i)) == 3 :
        print("Accession that contains any 3 numbers in any order:\t" + i)
    # contains 3 different numbers in the accession
    if len(set(re.findall(r'\d', i))) == 3 :
        print("Accession that contains 3 different numbers:\t" + i)
    # contain three or more numbers in a row
    if re.search(r'\d{3,}', i) :
        print("Accession that contains three or more numbers in a row:\t" + i)
    # end with d followed by either a, r or p
    if re.search(r'd[arp]$', i) :
        print("Accession that ends with d followed by either a, r or p:\t" + i)
