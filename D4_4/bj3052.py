import sys

sys.stdin = open('bj3052.txt', 'r')  

T = int(input())

for i in range(T) :
    numlist = []
    for i in range(10) :
        numlist.append(int(input())) 

    renlist = []
    for i in numlist :
        renlist.append(i%42)
        
    print(len(set(renlist)))