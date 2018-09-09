inputFile = open("snapin.txt", "r")
outputFile = open("snapout.txt", "w")

#Read
myInput = inputFile.read().split()

#get their position
Rose_Row = int(myInput[2])
Rose_column = int(myInput[3])
Scarlet_Row = int(myInput[4])
Scarlet_column = int(myInput[5])

#Small caculation to sure who will win
#Rule: If the difference of their Row and column have 1 odd number and 1 even
#number, Rose would win, if the difference have 2 even number, Scarlet would win
#, if two numbers are all odd number, Scarlet would win.

Row_difference = abs(Rose_Row - Scarlet_Row)
Column_difference = abs(Rose_column - Scarlet_column)

#Determine even or odd

if Row_difference%2 != 0 and Column_difference%2 == 0:
    outputFile.write("ROSE")
elif Row_difference%2 == 0 and Column_difference%2 != 0:
    outputFile.write("ROSE")
elif Row_difference%2 == 0 and Column_difference%2 == 0: 
    outputFile.write("SCARLET")
elif Row_difference%2 != 0 and Column_difference%2 != 0:
    outputFile.write("SCARLET")

#Close Files
inputFile.close()
outputFile.close()
