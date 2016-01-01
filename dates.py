from subprocess import Popen, PIPE

MONTHS = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sept","Oct","Nov","Dec"]
months = [1,2,3,4,5,6,7,8,9,10,11,12]
years = [2008,2009,2010,2011,2012,2013,2014,2014,2015]

dates = open("dates.csv",'w')


dates.write("start,end,month,year\n")
for i in range(0,len(years)):
    for j in range(0,len(months)):
        command = Popen(["date","--date="+str(months[j])+"/1/"+str(years[i])+"","+\'%s\'"],stdout=PIPE)
        start = command.communicate("")[0].decode().rstrip().replace("\'","")
        command = Popen(["date","--date="+str(months[j])+"/28/"+str(years[i])+"","+\'%s\'"],stdout=PIPE)
        end = command.communicate("")[0].decode().rstrip().replace("\'","")

        dates.write(start+","+end+","+MONTHS[j]+","+str(years[i])+"\n")




