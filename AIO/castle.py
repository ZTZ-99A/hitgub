inputFile = open("cavalryin.txt", "r")
outputFile = open("cavalryout.txt", "w")
myInput = inputFile.read().split()
number_of_knight = int(myInput[0])
a = 0
knights = []
for i in range(1,len(myInput)):
    knights.append(int(myInput[i]))
k = list(set(knights))
for i in range(0, len(k) ):
    if knights.count(k[i])%k[i] == 0 and a < len(k):
        a = a + 1
    if knights.count(k[i])% k[i] != 0 and a < len(k):
        outputFile.write("NO")
    elif knights.count(k[i])% k[i] == 0 and a == len(k):
        outputFile.write("YES")
    elif knights.count(k[i])% k[i] != 0 and a == len(k):
        outputFile.write("NO")
inputFile.close()
outputFile.close()
