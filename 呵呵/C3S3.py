#Open files
inputFile = open("tripin.txt", "r")
outputFile = open("tripout.txt", "w")

#Read data
myInput = inputFile.read().split()
triple_location = []

#Caculate remain
number_of_triple = 0
for i in range(0, len(myInput)):
    aim_number = int(myInput[i])
    location = i
    if aim_number % 3 == 0:
        number_of_triple = number_of_triple+1
        triple_location.append(location)
    if aim_number % 3 != 0:
        number_of_triple = number_of_triple
#write answer
if number_of_triple == 0:
    outputFile.write("Nothing here!")
else:
    outputFile.write(str(number_of_triple) + "\n")
#In order to write correctly
for i in range(0, len(triple_location)):
    outputFile.write(str(triple_location[i]) + " ")

#Close files
inputFile.close()
outputFile.close()