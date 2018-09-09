inputFile = open("probein.txt", "r")
outputFile = open("probeout.txt", "w")

#Read inputs
myInput = inputFile.read().split()
row = int(myInput[0])
column = int(myInput[1])
probe_row = int(myInput[2])
probe_column = int(myInput[3])
fissure_row = int(myInput[4])
fissure_column = int(myInput[5])
question = int(myInput[6]) * 2 + 7 #The end of the list

science=[]
for i in range(7, question):
    science.append(myInput[i])
i=0
count=0
while count < int(myInput[6]):
    a1 = int(science[i])
    a2 = int(science[i+1])
    i = i+2
    count = count+1
    if abs(probe_row-fissure_row) == abs(fissure_column-probe_column):
        if abs(a1-probe_row) + abs(a2-probe_column) < abs(a1-fissure_row) + abs(a2-fissure_column):
            outputFile.write('WATER'+'\n')
        if abs(a1-probe_row) + abs(a2-probe_column) > abs(a1-fissure_row) + abs(a2-fissure_column):
            outputFile.write('LAVA'+'\n')
        if abs(a1-probe_row) + abs(a2-probe_column) == abs(a1-fissure_row) + abs(a2-fissure_column):
            probe_int = max(abs(a1-probe_row), abs(a2-probe_column))
            fissure_int = max(abs(a1-fissure_row), abs(a2-fissure_column))
            if probe_int > fissure_int:
                outputFile.write('LAVA'+'\n')
            elif probe_int < fissure_int:
                outputFile.write('WATER'+'\n')
            elif probe_int == fissure_int:
                outputFile.write('MOUNTAINS'+'\n')
##############################################################################################################################
    else:
        if abs(a1-probe_row) + abs(a2-probe_column) < abs(a1-fissure_row) + abs(a2-fissure_column):
            outputFile.write('WATER'+'\n')
        if abs(a1-probe_row) + abs(a2-probe_column) > abs(a1-fissure_row) + abs(a2-fissure_column):
            outputFile.write('LAVA'+'\n')
        if abs(a1-probe_row) + abs(a2-probe_column) == abs(a1-fissure_row) + abs(a2-fissure_column):
            outputFile.write('MOUNTAINS'+'\n')            
inputFile.close()
outputFile.close()

