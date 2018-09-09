I = open("cloudin.txt", "r")
O = open("cloudout.txt", "w")
myInput = I.read().split()
k = int(myInput[1])
distances = myInput[2:len(myInput)+1]
distance = []
for i in range(0, len(distances)):
    distance.append(int(distances[i]))
value = []
cloud = 0
may = 0

for i in range(0, len(distance)):
    if k <= len(distance):
        may = sum(distance[i:k])
        k = k + 1
        value.append(may)
cloud = min(value)
O.write(str(cloud))
I.close()
O.close()
