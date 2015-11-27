from os import walk
from operator import itemgetter


print("Please input the folder to look in for the dates csv files")
folderName = input()

num = 0
tree = []
fileList = []


#Software Re-Use! :D
for root, dirs, files in walk(folderName):
    num = num + 1
    files = [f for f in files if not f[0] == '.']
    dirs[:] = [d for d in dirs if not d[0] == '.']
    tree.append((root,dirs,files))

for items in tree:
    for files in items[2]:
        fileList.append((str(items[0])+"/"+str(files),items[0], files))





d = {}  #dictionary of file names

for files in fileList:      #For every file we have to analyse

    f = open(files[0])
    lines = f.readlines()    #For every line

    lineCount = 0
    for line in lines:  #For every line get the filename and add it. count how many times its been added
        if lineCount == 0: 
            lineCount += 1
            continue
        key = line.split(",")[0].rstrip()
        if key not in d:
            d[key] = 1;
        else:
            d[key] += 1
        lineCount += 1

for k in sorted(d, key=d.get):
    print(k,d[k])



#FileList is now a list of all the csvs we have to work on!
