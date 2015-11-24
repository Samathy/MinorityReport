from py2neo import Graph

print("Please input the filename to put into Neo4J: ")
fileName = input()

f = open(fileName)

if  f == None:
    print("Couldent open file: "+fileName)


lines = f.readlines()
lines = [line.split(',') for line in lines]
print("Columns : ")
print(lines[0])

print("Connecting to Neo4J")
graph = Graph("http://neo4j:BigData@localhost:7474/db/data")
if graph == None:
    print("Couldent connect")
    quit()




