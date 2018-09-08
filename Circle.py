from math import pi


inputFile = open("circlein.txt", "r")
myInput = inputFile.read().split()


radius = int(myInput[0])


print("The area is:" + " " + str(radius**2 * pi))


inputFile.close()