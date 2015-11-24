from py2neo import Graph

def checkAuthor(name):  #Checks if the author already exists in the database.
    name = strip_punctuation(name) #Should remove all special chars
    query = graph.cypher.execute("MATCH( person{name:'"+str(name)+"'}) RETURN(person)")
    if query.one == None:        #If there are no records with that name value
        print("Author: "+name+" Already exists")
        return False            #Return falsch
    else:
        return True
    return

def checkDate(date):
    query = graph.cypher.execute("MATCH(Date{date:'"+str(date)+"'}) RETURN(date)")
    if query.one == None:
        return False
    else:
        return True

def checkProduct(projName):     #Checks if project already exists
    query = graph.cypher.execute("MATCH(Project{name:'"+str(projName)+"'}) RETURN(Project)")
    if query.one == None:
        return False
    else:
        return True

def checkComponant(comName):    #Checks if Conponants already exists
    query = graph.cypher.execute("MATCH(Componant{name:'"+str(comName)+"'}) RETURN(Componant)")
    if query.one == None:
        return False
    else:
        return True

    
def addAuthor(name):            #Adds a new author..
    print("Adding Author: "+name)
    name = strip_punctuation(name) #Should remove all special chars
    query = graph.cypher.execute("CREATE (p:Person{name: '"+str(name)+"'}) RETURN p")
    return

def  addProduct(projName):      #Adds new Project
    query = graph.cypher.execute("CREATE (p:Product{name:'"+projName+"'}) RETURN p")
    return

def addComponant(comName):      #Adds new conponant and links to the project its part of.
    query = graph.cypher.execute("MATCH (p:Product) WHERE p.name = '"+product+"' CREATE (c:Componant{name:'"+comName+"'}) -[r:Part_of]->(p) RETURN c")
    return

def addDate(date):
    query = graph.cypher.execute("CREATE (d:Date{date: '"+str(date)+"'})RETURN d")
    return 

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

for line in lines:
    line




