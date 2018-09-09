inputFile = open("streetin.txt","r")
outputFile = open("streetout.txt","w")
myInput = inputFile.read().split()
street = int(myInput[0])
park = int(myInput[1])
ans = 0
if street == park:
    ans = 0
elif street != park:
    ans = int(street/(park+1))
outputFile.write(str(ans))
inputFile.close()
outputFile.close()
