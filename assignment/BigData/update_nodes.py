from py2neo import Graph

try:
    graph =  Graph("http://neo4j:BigData@localhost:7474/db/data/")
except ConnectionRefusedError:
    print ("Couldent connect to Neo4J - Did you start the DB>")
    quit()


files = open("Sorted_People.csv")        #Open the sorted data files

lines = files.readlines()

lineCount = 0

for line in lines:

    if lineCount == 0:
        lineCount +=1
        continue

    filename = line.split(",")[0]

    print("Updating file: "+filename)

    query = graph.cypher.execute(" \
	MERGE (p:Person{name:\'"+filename+"\'}) \
	ON MATCH SET p.HighRisk = True \
	RETURN p")
    print(query)

