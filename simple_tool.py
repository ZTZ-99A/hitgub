#This is a simple tool to do many thing
def triple_sum(a, b, c):
    if a == b == c:
        return(9 * a)
    else:
        return(a + b + c)
    
#Find the number of element in a list
def find_element(n, b):
    count = 0
    for i in b:
        if i == n:
            count = count+1
    return count

#Find even or odd elements in a list
def find_even_element(l):
    even = []
    for i in l:
        if i % 2 == 0:
            even.append(i)
    return even

#Find even elements which is smaller than a number a.
def smart_find_even(l, a):
    even = []
    for i in l:
        if i < a and i % 2 == 0:
            even.append(i)
    return even

#How to find the distance between point (x1, y1) and (x2,y2)
def find_distance(a, b, c, d):
    return ((a - c) ** 2 + (b - d) ** 2) ** 0.5

#How to caculate the sum of the first n positive integers
def arithmeti_sequence(a, b):
    return int(((a + b) * (b - a + 1)) / 2)

            