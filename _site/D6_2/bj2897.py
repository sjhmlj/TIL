import sys
sys.stdin = open('bj2897.txt', 'r')

r, c = list(map(int, input().split()))

parking = [list(input())for i in range(r)]
result = [ 0 for i in range(5)]
dxy = [
    [0 , 0],
    [1 , 0],
    [0 , 1],
    [1 , 1]

]
for i in range(r-1) :
    for j in range(c-1) :
        if parking[i][j] != '#' :
            cnt = 0
            for k in range(4) :
                nr = i + dxy[k][0]
                nc = j + dxy[k][1]
                if 0<= nr <= r and 0<= nc <= c :
                    if parking[nr][nc] == 'X' :
                        cnt += 1
                    elif parking[nr][nc] == '#' :
                        cnt = -1 
                        break
            if cnt != -1 :
                result[cnt] += 1
            # print(i, j, cnt)

for i in result :
    print(i)


