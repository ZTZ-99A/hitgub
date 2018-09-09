#Open files
inputFile = open("wetin.txt", "r")
outputFile = open("wetout.txt", "w")

#Read data
myInput = inputFile.read().split()

#Transform to integer
myInput = [int(i) for i in myInput]
container = 0

#Caculate
for i in range(len(myInput)):
    rainfall = myInput[i]
    value = container + rainfall
    if value >= 10:
        container =  value - 10
    elif value < 10:
        container = 0
        
#Write answer
outputFile.write(str(container))

#Close files
inputFile.close()
outputFile.close()