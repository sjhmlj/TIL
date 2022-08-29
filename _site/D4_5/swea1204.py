import sys

sys.stdin = open('swea1204.txt', 'r')

T = int(input())

for i in range(T):
    sequence = int(input())

    num = list(map(int, input().split()))
    numdic = {}
    for i in num :
        numdic[i] = 0
    for i in num :
        numdic[i] += 1
    
    max_num = max(numdic.values())
    result = []
    for i in numdic :
        if numdic[i] == max_num :
            result.append(i)

    print(f'#{sequence} {result[0]}')
