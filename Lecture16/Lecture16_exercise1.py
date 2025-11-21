#!/usr/bin/python3

# Lecture 16, Exercise 1: Interrogating the user
# Written by Grace Newman (s2823303) on 20 November 2025

# With the aid of a function and a dictionary, write an interactive Python programme/script that will ask the user the following questions
# - What's your name?
# - How old are you?
# - What is your favourite colour?
# - Do you like Python?
# - The world is flat: True or False?
# and then, based on their answers, make some comments back to them (this doesn't have to be at all serious, it's the methods used that we are trying out here....!)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

import sys, os

os.system('clear')
print ("\n\nImported os\nImported sys\n\n")


# A function to respond to the user's details.
def interrogate(name, age, col, py, world):
    import string
    print("\nYou have provided the following details:\n\tName: ",name,"\n\tAge: ",age,"\n\tFave colour: ",col,"\n\tPython preference: ",py,"\n\tFlat world: ",world)
    for character in name:
        if character not in string.ascii_letters :
            return print("\nInvalid name, please start again.") # function will end
    if age > 130 or age < 0 :
        print("\n"+ name + ", I really dont think your age is credible, do you?")
    if age > 0 and age < 18 :
        print("\n"+ name + ", you are a child, please get parental permission to continue.")
    if col.upper() == "BLUE" :
        print("\nBlue is the correct choice, good job.")
    elif col.upper() == "RAINBOW":
        print("\nYou're GAY!")
    else:
        print("\n The color, " +col+" , is nice, but it's not the best one.")
    if py.upper()[0] != "Y" :
       print("\nI am sorry that you don't like Python.")
    else :
       print("\nGlad you agree that Python is cool...")
    if world != "False" :
       return print("\nEither you really DO think the world is flat (it isn't),\nor you haven't typed False in the correct Python format...\n\n")
    return "OK",print("\nAll OK, thanks a lot.")

# Interact with the user, storing the output into an ordered dictionary.
details = {}
details["Name"] = input("What is your name?\t")
details["Age"] = int(input("How old are you?\t"))
details["Color"] = input("What is your favorite color?\t")
details["Python"] = input("Do you like Python?\t")
details["World"] = input("The world is flat: True of False?\t")

interrogate(*list(details.values()))

print("\n\nThis was the dictionary you set up...\n\n",details,"\n\nBye!\n\n")
