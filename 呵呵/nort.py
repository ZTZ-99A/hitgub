#create files
inputFile = open("nortin.txt", "r")
outputFile = open("nortout.txt", "w")

#Read data
myInput = inputFile.read().split()

#W means width, H means height
W = int(myInput[0])
H = int(myInput[1])
longest = 0
#Rule 1: If one of the W and H are even number, the longest possible = W * H
#Rule 2: If both of them are odd number, the longest possible = W * H - 1
if W%2 == 0 or H%2 == 0:
    longest = W * H
elif W%2 ==1 and H%2 == 1:
    longest = W * H - 1

#Write answer
outputFile.write(str(longest))

#close files
inputFile.close()
outputFile.close()
