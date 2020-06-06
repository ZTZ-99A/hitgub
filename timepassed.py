def timepassedmidnight(time):
    hour = time // 3600
    minute = time // 60
    print(str(hour) + " " + str(minute))

def timepassedevent(h1,m1,s1,h2,m2,s2):
    print(str((h2 - h1) * 3600 + (m2 - m1) * 60 + (s2 - s1)* 1))

def pointdist(x1, y1, x2, y2):
    print(str((abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)**0.5))

def leap(year):
    if year % 400 == 0:
        print("LEAP")
    elif year % 4 == 0 and year % 100 != 0:
        print("LEAP")
    else:
        print("COMMON")

def JugMugPugs(n):
    threediv = n % 3
    fivediv = n % 5
    sevendiv = n % 7
    num = str(n)
    boolean = [0, 0, 0]
    boolean_2 = [0, 0, 0]
    for i in num:
        if i == '3':
            boolean[0] = 1
        elif i == '5':
            boolean[1] = 1
        elif i == '7':
            boolean[2] = 1
    if threediv == 0:
        boolean_2[0] = 1
    if fivediv == 0:
        boolean_2[1] = 1
    if sevendiv == 0:
        boolean_2[2] = 1
    if boolean[0] == 1 or boolean_2[0] == 1:
        print('Jugs',end = "")
    if boolean[1] == 1 or boolean_2[1] == 1:
        print('Mugs', end = "")
    if boolean[2] == 1 or boolean_2[2] == 1:
        print('Pugs', end = "")
    else:
        print(num)

def printout(message):
    length = len(message)
    print(message[2])
    print(message[length - 2])
    print(message[0:5])
    print(message[0:length - 2])
    even = [ ]
    for i in range(0,length):
        if i%2 == 0:
            even.append(message[i])
    for i in even:
        print(i,end = "")
    print('\n',end = "")
    for i in range(0,length):
        if i%2 != 0:
            print(message[i],end = "")
    print('\n',end = "")
    for i in range(length - 1,-1,-1):
        print(message[i],end = "")
    print("\n",end = "")
    for i in range(len(even) - 1, -1,-1):
        print(even[i], end = "")
    print("\n", end = "")
    print(length)
        
def removeh(message):
    convert = [ ]
    for i in range(0, len(message)):
        if 'h' == message[i]:
            convert.append(i)
    first_h = convert[0]
    last_h = convert[-1]
    print(message[0:first_h],end = "")
    print(message[last_h + 1:len(message)])

def reverseh(message):
    convert = [ ]
    for i in range(0, len(message)):
        if 'h' == message[i]:
            convert.append(i)
    first_h = convert[0]
    last_h = convert[-1]
    print(message[0:first_h+1],end = "")
    print("".join(reversed(message[first_h : last_h])),end = "")
    print(message[last_h + 1:len(message)])

def dilateh(message):
    convert = [ ]
    for i in range(0, len(message)):
        if 'h' == message[i]:
            convert.append(i)
    first_h = convert[0]
    last_h = convert[-1]
    convert.pop()
    del convert[0]
    for i in range(0, len(message)):
        if i in convert:
            print("H", end = "")
        else:
            print(message[i], end ="")

def seclargest(sequences):
    sequences.sort()
    print(sequences[len(sequences)-2])

def printeven(sequence):
    for i in range(0, len(sequence)):
        if i%2 == 0:
            print(sequence[i], end  = " ")

def showeven(sequence):
    for i in sequence:
        if i%2 == 0:
            print(i, end  = " ")

def rightlargerleft(sequence):
    for i in range(0, len(sequence) - 1):
        left = sequence[i]
        right = sequence[i + 1]
        if left < right:
            print(right, end  = " ")

def samesign(sequence):
    first_pair = [ ]
    for i in range(0, len(sequence) - 1):
        left = sequence[i]
        right = sequence[i + 1]
        if left * right > 0:
            first_pair.append(left)
            first_pair.append(right)
            break
    if len(first_pair) == 2:
        for i in first_pair:
            print(i, end  = " ")
    else:
        print(0)

def midlargest(sequence):
    mid = []
    for i in range(1,len(sequence) - 1):
        left = sequence[i - 1]
        midn = sequence[i]
        right = sequence[i + 1]
        if midn > left and midn > right:
            mid.append(midn)
    print(len(mid))
            
    

    
