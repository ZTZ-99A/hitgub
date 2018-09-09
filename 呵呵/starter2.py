inputFile=open("sitin.txt","r")
outputFile=open("sitout.txt","w")
myInput=inputFile.read().split()
r=int(myInput[0])
s=int(myInput[1])
attend=int(myInput[2])
cap=r*s
standing=attend-cap
if standing>0:
    sit=cap
else:
    standing=0
    sit=attend
outputFile.write(str(sit)+" "+str(standing))
inputFile.close()
outputFile.close()
