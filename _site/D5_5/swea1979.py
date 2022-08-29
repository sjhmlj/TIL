from re import L
import sys
sys.stdin = open('swea1979.txt', 'r')


T = int(input())
for t in range(1, T+1) :
    n, k = list(map(int,input().split()))

    puzzle = [list(map(int,input().split())) for i in range(n)]


    result = 0
    for i in range(n) :

        cnt = 0
        for j in range(n) :
            if puzzle[i][j] == 1 :
                cnt += 1
                if j == n-1 :
                    if cnt == k :
                        result += 1          
            else :
                if cnt == k :
                    result += 1
                cnt = 0

        cnt = 0
        for f in range(n) :
            if puzzle[f][i] == 1 :
                cnt += 1
                if f == n-1 :
                    if cnt == k :
                        result += 1
            else :     
                if cnt == k :
                    result += 1
                cnt = 0

    print(f'#{t} {result}')
    # break
            