#As normal
inputFile = open("taktakin.txt","r")
outputFile = open("taktakout.txt","w")
myInput=inputFile.read().split()
fruits=int(myInput[0])
#define
fullmoon=0
#caculate
while fruits%11 !=1:
    fruits=fruits*2
    fullmoon=fullmoon+1
else:
    outputFile.write(str(fullmoon)+" "+str(fruits))
#close files
inputFile.close()
outputFile.close()
