from py2neo import Graph

try:
    graph =  Graph("http://neo4j:BigData@localhost:7474/db/data/")
except ConnectionRefusedError:
    print ("Couldent connect to Neo4J - Did you start the DB>")


query = graph.cypher.execute("MATCH (f:File)<-[:Applied_too]-(c:Commit)-[:Commit_date]->(d:Date) WHERE d.date >= "1438383600" RETURN DISTINCT f")

f = open("recent_files.csv")

for nodes in query:
    query[

