#Open files
inputFile = open("dishin.txt", "r")
outputFile = open("dishout.txt", "w")

#Read data
myInput = inputFile.read().split()
data = []
sum_of_number = 0

#Transform string into integer
for i in range(1, len(myInput)):
    number = int(myInput[i])
    data.append(number)

#Caculate mean by loop
for i in range(0, len(data)):
    aim_number = data[i]
    sum_of_number = sum_of_number + aim_number
mean = int(sum_of_number / len(data))
outputFile.write(str(min(data)) + " " + str(max(data)) + " " + str(mean))
inputFile.close()
outputFile.close()