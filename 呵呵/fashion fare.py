#Open files
inputFile = open("fashin.txt", "r")
outputFile = open("fashout.txt", "w")

#Read files
myInput = inputFile.read().split()
fare = int(myInput[0])

#Caculate
notes = 0

a = int(fare / 100)
a_int = fare % 100
b = int(a_int / 20)
b_int = a_int % 20
c = int(b_int / 5)
c_int = b_int % 5

notes = a + b + c + c_int

#Write answer
outputFile.write(str(notes))

#Close files
inputFile.close()
outputFile.close()

