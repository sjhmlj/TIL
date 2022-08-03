import sys

sys.stdin = open('zbj10816.txt', 'r') 

N = int(input())          #! 인풋이 500000까지 나온다. O(n^2)은 통과 못한다. 
numdic = {}
# for i in range(N) :
num = input().split()





M = int(input())

# for i in range(M) :
vsnum = input().split()
for i in vsnum :
    numdic[i] = 0
for i in num :
    numdic[i] = 0
for i in num :
    numdic[i] += 1
print(numdic)

for i in vsnum :
    print(numdic[i], end= ' ')