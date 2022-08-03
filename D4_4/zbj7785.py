from re import L
import sys

sys.stdin = open('zbj7785.txt', 'r') 

T = int(input())
memberdic = {}
for i in range(T) :
    a, b = input().split()

    memberdic[a] = b
cnt = 0
memberlist = list(memberdic.keys())
for i in memberlist :
    if memberdic[i] == 'leave' :
        memberdic.pop(i)
nowmember= sorted(memberdic.keys())
nowmember.reverse()
for i in nowmember :
    print(i)

