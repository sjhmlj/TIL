import sys
sys.stdin = open('bj2178.txt', 'r')



n, m = list(map(int, input().split()))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

miro = [list(map(int, input()))for i in range(n)]
i, j = 0, 0
stack = []
while True:


    if (i, j) ==(n-1, m-1) :
        print(miro[i][j])
        break


    # stack.append((i, j, miro[i][j]))    ## 방금 전의 인덱스를 저장
    next = [] ## 이동할 곳의 인덱스 저장. 
    vs = miro[i][j]
    for k in range(4) :
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx <= n-1 and 0 <= ny <= m-1 :
            if miro[nx][ny] == 0 :
                continue
            else :
                if miro[nx][ny] == 1 :
                    stack.append((nx, ny))
                    if nx == 0 and ny == 0 :
                        pass
                    else :
                        miro[nx][ny] = miro[i][j] + 1
                        next.append((nx, ny))

                elif miro[nx][ny] > 1 :
                    miro[nx][ny] = min(miro[i][j]+1, miro[nx][ny])
                    
                    if miro[nx][ny] > vs :
                        vs = miro[nx][ny]
                        next.append((nx, ny))
                stack.append((nx, ny))
                while True :
                    if len(next) != 0 :
                        break 
                    next.append(stack.pop())

    # a, b, c = stack.pop()
    # miro[a][b] = c

    i, j = next[-1][0], next[-1][1]
    # print(i, j)
    # break
# print(miro[i][j])

        


    