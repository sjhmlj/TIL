from re import L
import sys
sys.stdin = open('bj5533.txt', 'r')

n = int(input())

score = [[], [], []]
for i in range(n) :
    a, b, c = list(map(int, input().split()))
    score[0].append(a)
    score[1].append(b)
    score[2].append(c)

# print(score)

result = [0 for i in range(n)]
for i in range(3) :
    for j in range(n) :
        num = score[i][j] 
        if score[i].count(num) != 1 :
            num = 0
        result[j] += num

# print(result)
for i in result :
    print(i)

