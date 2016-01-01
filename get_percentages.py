f = open("Sorted_Files.csv")
j = open("File_Percentages.csv",'w')


lines = f.readlines()

lineCount = 0

percentages = []

print("How many months were there?")
total = input()

print(int(total))


for line in lines:
    if lineCount == 0:
        lineCount +=1
        continue
    num = line.split(",")[1]
    fi = line.split(",")[0]
    percentages.append((fi,str(int((int(num)/int(total))*100))+"%"))
    print(str((int(total)/int(num))*100))



print(percentages)
for i in percentages:
    j.write(i[0]+","+i[1]+"\n")


f.close()
j.close()

