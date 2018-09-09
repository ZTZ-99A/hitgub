#As normal
inputFile=open("countin.txt","r")
outputFile=open("countout.txt","w")
myInput=inputFile.read().split()
number=int(myInput[0])
count=1
#loop
while count <= number:
    outputFile.write(str(count)+"\n")
    count=count+1
#close files
inputFile.close()
outputFile.close()
