#Open files
inputFile = open("rainin.txt", "r")
outputFile = open("rainout.txt", "w")

#Read data
myInput = inputFile.read().split()
volume_of_tank = int(myInput[1])
rain_report = []

#Transform data to integer
for i in range(2, len(myInput)):
    number = int(myInput[i])
    rain_report.append(number)
    
#Caculate by loop
in_volume = 0
days = 0
index = 0
while in_volume < volume_of_tank:
    rain = rain_report[index]
    in_volume = in_volume + rain
    days = days + 1
    index = index + 1
    
#write answer
outputFile.write(str(days))

#close files
inputFile.close()
outputFile.close()