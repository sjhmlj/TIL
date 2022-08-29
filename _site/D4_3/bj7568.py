from re import L
import sys

sys.stdin = open('bj7568.txt', 'r')       


T = int(input())


weightlist = []
heightlist = []
for i in range(T) :
    a, b= list(map(int, input().split()))
    resultlist = []
    weightlist.append(a)
    heightlist.append(b)
    

   
# print(weightlist)
# print(heightlist)

for i in range(T) :
    cnt = 0
    for j in range(T) :
        if weightlist[j] > weightlist[i] and heightlist[j] > heightlist[i] :
            cnt += 1
    resultlist.append(cnt+1)

for i in resultlist :
    print(i, end= ' ')