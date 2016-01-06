import os

#####
#   Short note about how i'm gonnado the setup and config files:
#   We're going to have a folder of files, each one being its own setup file for the csv import, and Git2Neo git import.
#   That way the user can set things up on their own.



f = open("MinorityProcess.txt")     #Open the spec


Lines = f.readlines()

lineCount = 0

for line in Lines:

    if line == "repoPath":      #Get the repo
        repoPath == Lines[lineCount+1]
    elif line == "folder":              #Get the folder of files listing each componant
        folder = Lines[lineCount+1]
    
    lineCount += 1


for files in os.listdir(os.getcwd()):
    next



print("This is Minority Report. I will start by importing your bugs into Neo4J.")

import csv_to_Neo4J

print("Now importing Git data")

#import Git2Neo     #Need to make git2neo a proper module first, then I can just import the directory its cloned into.
#git2neo.main()




