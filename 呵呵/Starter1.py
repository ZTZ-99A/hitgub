inputFile=open("addin.txt","r")
outputFile=open("addout.txt","w")
myInput = inputFile.read().split()
num_1=int(myInput[0])
num_2=int(myInput[1])
ans=num_1+num_2
outputFile.write(str(ans)+"\n")
inputFile.close()
outputFile.close()
