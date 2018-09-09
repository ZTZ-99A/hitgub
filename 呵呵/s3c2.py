inputFile=open("dictin.txt","r")
outputFile=open("dictout.txt","w")
myInput=inputFile.read().rstrip("\n")
a=myInput.split("\n")
b = []
list_a = []
list_b = []
list_1 = []
list_2 = []
list_3 = []
for i in range(len(a)):
    b.append(a[i].split())
for s in range(1,len(b)):
    if len(b[s])==2:
        list_a.append(b[s])
    else:
        list_b.append(b[s])
for maus in range(len(list_a)):
    list_1.append(list_a[maus][0])
for second in range(len(list_a)):
    list_2.append(list_a[second][1])
for minute in range(len(list_b)):
    list_3.append(list_b[minute][0])
for jiang in list_3:
    if jiang in list_1:
        index=list_1.index(jiang)
        outputFile.write(list_2[index]+"\n")
    else:
        outputFile.write("C?\n")
inputFile.close()
outputFile.close()
