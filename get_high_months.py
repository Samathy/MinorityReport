###############3
#   This script should get all the high bug months for a given sub-componant,

#   I,e it writes the months which are deemed as high bug months to a file


#TODO Currently this just map-reduces all the dates, we need to make it so it does it by month/year only.


if __name__ == "__main__":
    return


def main(connectionString, subComponant):

    try:
        graph = Graph(connectionString)
    except:
        print("Could not connect to Neo4J database")

    #Get every date for every bug for our subcomponant
    query  = graph.cypher.execute("MATCH (c:Componant{name:\""+subComponant+"\'}) -- (f:Bug) -- (d:Date) RETURN c,f LIMIT 25")

    if query.one == None:       #If there was nothing returned..get out.
        print("No dates!")
        return false

    out = Open(subComponant+" - AllDates.csv","w")

    for q in query: #For every node that we got
        out.write(q.n["date"])  #Write out the date of that


    close(out)


#MapReduce that!

f = open(subComponant+" - AllDates.csv","r")
lines = f.readlines()    #For every line

lineCount = 0
for line in lines:  #For every line get the date and add it. count how many times its been added
    if lineCount == 0: 
        lineCount += 1
        continue
    key = line.split(",")[0].rstrip()
    if key not in d:
        d[key] = 1;
    else:
        d[key] += 1
    lineCount += 1

out = open("Sorted_Dates.csv",'w')

out.write("Date,Occurances\n")
for k in sorted(d, key=d.get, reverse=True):
print(k,d[k])
out.write(k+","+str(d[k])+"\n")

out.close()





