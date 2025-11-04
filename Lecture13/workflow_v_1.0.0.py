#!/usr/bin/python3
# Workflow programme v_1.0.0 and report
# Written by s2823303 on Thursday 30 October 2025
# Take a list and make files from each element, writing out the length to the file,
# and printing the first 3 characters in upper case
# Step 1 : Generate the input list
somecolours4 = ['blue','red','green']

# Step 2 : Loop through the list
# the loop body contains all the actions required
for colour_item in somecolours4 :
    myfile = open(colour_item + '.txt', 'w')
    myfile.write(str(len(colour_item)) + '\n')
    myfile.close()
    f'{colour_item[0:3].upper()}'
