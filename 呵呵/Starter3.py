inputFile = open("mixin.txt","r")
outputFile = open("mixout.txt","w")
myInput=inputFile.read().split()
#sure the number
n=int(myInput[0])
d=int(myInput[1])
#caculate
a=int(n/d)
b=n%d
#To sure the number
if b>0:
    outputFile.write(str(a)+" "+str(b)+"/"+str(d))
else:
    outputFile.write(str(a))
inputFile.close()
outputFile.close()
