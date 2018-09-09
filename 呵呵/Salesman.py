#Open files
inputFile = open("salesin.txt", "r")
outputFile = open("salesout.txt", "w")

#Read data
myInput = inputFile.read().split()

#Sure routes
route_1 = int(myInput[0])
route_2 = int(myInput[1])
route_3 = int(myInput[2])

#Caculate
ans = max(route_1 + route_2, route_2 + route_3, route_3 + route_1)

#Write answer
outputFile.write(str(ans))

#Close files
inputFile.close()
outputFile.close()