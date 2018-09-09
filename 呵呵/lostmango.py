inputFile = open("manin.txt","r")
outputFile = open("manout.txt","w")
myInput=inputFile.read().split()
#Read
a=int(myInput[0])
b=int(myInput[1])
c=int(myInput[2])
d=int(myInput[3])
#caculate
v1=a+c
v2=b+d
v3=a-c
v4=b-d
#Meansure
if v1==v2:
    outputFile.write(str(v1))
elif v3==v4:
    outputFile.write(str(v3))
elif v1==v4:
    outputFile.write(str(v4))
elif v2==v3:
    outputFile.write(str(v2))
inputFile.close()
outputFile.close()
