from py2neo import Graph
from subprocess import Popen, PIPE
import time


datesFile = open("dates.csv")

savedDates = datesFile.readlines()


minDates = []
maxDates = []

MONTHS = []
years = []




count = 0
for line in savedDates:  #For every line in the dates
    if count == 0:
        count += 1
        continue

    minDates.append(line.split(",")[0].rstrip())     #get the min date
    maxDates.append(line.split(",")[1].rstrip())     #get the max date
    MONTHS.append(line.split(",")[2].rstrip())
    years.append(line.split(",")[3].rstrip())

    count += 1


print("Enter filename of list of months to analyise")
fileName = input()

toAnalyse = open(fileName)
filedates = toAnalyse.readlines()

dates = []

lineCount = 0

print(filedates)

for line in filedates:  #for every entered date
    print("matching "+line)
    for ds in savedDates:   #for every saved date
        if ds.split(",")[2] == line.split(",")[0] and ds.split(",")[3] == line.split(",")[1]:
           dates.append((savedDates[lineCount].split(",")[0],savedDates[lineCount].split(",")[1],savedDates[lineCount].split(",")[2],savedDates[lineCount].split(",")[3])) #if we've found a date we need, add it to the list
           dates.append((savedDates[lineCount-1].split(",")[0],savedDates[lineCount-1].split(",")[1],savedDates[lineCount-1].split(",")[2],savedDates[lineCount-1].split(",")[3])) #if we've found a date we need, add it to the list
           dates.append((savedDates[lineCount-2].split(",")[0],savedDates[lineCount-2].split(",")[1],savedDates[lineCount-2].split(",")[2],savedDates[lineCount-2].split(",")[3])) #if we've found a date we need, add it to the list
           break
        lineCount+=1
    lineCount = 0

print(dates)

try:
    graph =  Graph("http://neo4j:BigData@localhost:7474/db/data/")
except ConnectionRefusedError:
    print ("Couldent connect to Neo4J - Did you start the DB>")


querys = []

for date in dates:

    f =  open("files_Committed_Too_During/"+date[2]+"-"+date[3].rstrip()+".csv",'w')
    f.write("Filename, Commit Count, Month, Year\n")
    query = graph.cypher.execute("MATCH (f:File)<-[:Applied_too]-(c:Commit)-[r:Commit_date]->(d:Date), (p:Person)-->(c) WHERE d.date >= \""+date[0]+"\" AND d.date <= \""+date[1]+"\" RETURN DISTINCT f AS File ,COUNT(c) AS CommitCount")

    if query == None:
        f.close()
        continue

    for fi in query:
        f.write(fi["File"]["name"]+","+str(fi["CommitCount"])+","+str(date[2])+","+str(date[3]))
    
    f.close()



    #From this we get all the committers to the files, as well as all the files committed over the months prior to the bugs occurring.
    #We could buid a query wcich returns only one instance of the file using collect(f)
    #We need to group up the files and see if we can recognise any that come up a lot.
    #We can also start looking at committers that come up a lot.
    #Maybe we can exclude Linus though, since a lot of his commits are merges.
    




