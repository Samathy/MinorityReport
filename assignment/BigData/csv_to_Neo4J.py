from py2neo import Graph
from subprocess import Popen, PIPE


class Bug:
    uid = ""
    product = ""
    componant = ""
    status = ""
    resolved = ""
    date = ""
    kernel = ""


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
    print("checking date:")
    print(date)
    query = graph.cypher.execute("MATCH(Date{date:'"+str(date)+"'}) RETURN(Date)")
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
    print("Chcking Componant")
    query = graph.cypher.execute("MATCH(Componant{name:'"+str(comName)+"'}) RETURN(Componant)")
    if query.one == None:
        return False
    else:
        return True

def checkKernel(kernel):    #Checks if Conponants already exists
    query = graph.cypher.execute("MATCH(Kernel{name:'"+str(kernel)+"'}) RETURN(Kernel)")
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
    query = graph.cypher.execute("CREATE (d:Date{date:'"+str(date)+"'})RETURN d")
    return 

def addKernel(kernel):
    query = graph.cypher.execute("CREATE (d:Kernel{name: '"+str(kernel)+"'})RETURN d")
    return


def addBug(bug):

    if checkDate(bug.date) == False:
        print("Adding date")
        addDate(bug.date)
    if checkKernel(bug.kernel) == False:
        print("Adding kernel")
        addKernel(bug.kernel)
    if checkComponant(bug.componant) == False:
        print("adding componant")
        addComponant(bug.componant)

    #TODO Add rest of query content

    query = graph.cypher.execute("MATCH (d:Date), (k:Kernel), (c:Componant) \
    WHERE d.date = '"+bug.date+"' AND k.name = '"+bug.kernel+"' AND c.name = '"+bug.componant+"' \
    CREATE (b:Bug{uid:'"+str(bug.uid)+"',status:'"+bug.status+"'}) \
            CREATE (b)-[od:Opened_date]->(d) \
            CREATE (b)-[fi:Found_in]->(k) \
            RETURN b")

            #CREATE (b)-[od:Opened_date]->(d) \
            #CREATE (b)-[ob:Opened_by]->(p) \
            #CREATE (b)-[fi:Found_in]->(k) \
    print(query)
    if query.one == None:
        print("Something went wrong")




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
graph = Graph("http://neo4j:BigData@localhost:7474/db/data/")
if graph == None:
    print("Couldent connect")


count = 0

product = "File Systems"
componant = "ext4"

for line in lines:

    if count == 0:
        count += 1
        continue

    bug = Bug()
    bug.uid = line[0].replace("\"","")
    bug.product = product
    bug.componant = componant
    bug.status = line[6].replace("\"","")
    bug.kernel = line[8].replace("\"","")
    
    #Need to do a bit of hacky processing to get the date right
    command = Popen(["date","--date="+line[10].replace("-","/").replace("\"","")+"","+\'%s\'"],stdout=PIPE)
    date = command.communicate("")[0].decode()
    bug.date = date.replace("\'","")

#    print(bug)
    addBug(bug)

    count += 1

print("Added "+str(count)+" Bugs")


