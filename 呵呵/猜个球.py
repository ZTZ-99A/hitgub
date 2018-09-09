#Open files
inputFile = open("handin.txt", "r")
outputFile = open("handout.txt", "w")

#Read files
myInput = inputFile.read().split()

#get data
cup_have_ball = int(myInput[1])
#k means the times of swaps
k = int(myInput[2])
#translate data
cup_swap = []
for i in range(3, len(myInput)):
    cup_swap.append(myInput[i])
#CACULATION RULE
i = 0
while i < k*2:
    swap_cup = int(cup_swap[i])
    aim_cup = int(cup_swap[i+1])
    i = i+2
    if swap_cup < cup_have_ball and aim_cup > cup_have_ball:
        cup_have_ball = cup_have_ball - 1
    elif swap_cup < cup_have_ball and aim_cup < cup_have_ball:
        cup_have_ball = cup_have_ball
    elif swap_cup > cup_have_ball and aim_cup > cup_have_ball:
        cup_have_ball = cup_have_ball
    elif swap_cup > cup_have_ball and aim_cup < cup_have_ball:
        cup_have_ball = cup_have_ball + 1
    elif swap_cup == cup_have_ball:
        cup_have_ball = aim_cup
    elif swap_cup < cup_have_ball and aim_cup == cup_have_ball:
        cup_have_ball = cup_have_ball - 1
    elif swap_cup > cup_have_ball and aim_cup == cup_have_ball:
        cup_have_ball = cup_have_ball + 1
ans = str(cup_have_ball)
#ENTER ANSWER
outputFile.write(ans)
#CLOSE FILE
inputFile.close()
outputFile.close()
