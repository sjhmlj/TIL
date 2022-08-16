import sys
from pprint import pprint
sys.stdin = open("test.txt")
import copy
T = int(input())

for t in range(1, T+1) :
    n, k = map(int, input().split())

    mt = []
    top_mt = 0
    for i in range(n) :
        mt.append(list(map(int, input().split())))
        if top_mt < max(mt[i]) :
            top_mt = max(mt[i])
    dxy = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]
    mt2 = copy.deepcopy(mt)
    def dfs_mt(node1, node2) :
        
        result = 1
        visited = [[0]*n for i in range(n)]
        for clap in range(1, top_mt+1) :
            stack = [[node1, node2, 1]]
            stack2 = []
            while stack :
                if len(stack) >= 2 :

                    if stack[-1][2] > stack[-2][2] :
                        y2, x2, cnt2 = stack2.pop()
                        visited[y2][x2] = 0

                y, x, cnt = stack.pop()
                visited[y][x] = 1

                

                if cnt-1 == clap:
                    mt[y][x] -= k

                len_stack = len(stack)

                for i in range(4) :
                    ny = y + dxy[i][0]
                    nx = x + dxy[i][1]

                    if 0<= ny <= n-1 and 0<= nx <= n-1 :    

                        if not visited[ny][nx] :
                            if cnt == clap and mt[ny][nx] >= k : 
                                if mt[ny][nx]-k < mt[y][x] :
                                    stack.append([ny, nx, cnt+1])
                                    if result < cnt+1 :
                                        result = cnt+1
                            elif mt[ny][nx] < mt[y][x] :
                                # if node2 == 3 :
                                #     print(mt[ny][nx], mt[y][x])
                                stack.append([ny, nx, cnt+1])
                                
                                if result < cnt+1 :
                                    result = cnt+1
                                
                                    # print('ny :', ny,'nx :', nx,'result :', result,'mt[ny][nx] :', mt[ny][nx], 'mt[y][x] :', mt[y][x])

                # 초기화 단계
                if cnt-1 == clap :
                    mt[y][x] += k

                if len_stack == len(stack) :
                    visited[y][x] = 0
                    
                else :
                    stack2.append([y, x, cnt])

                

                # if node2 == 3 :
                    # print(y, x, mt[y][x], cnt, clap)
                    # print(stack)
                # pprint(stack)
            if result < clap :
                return result
            if node2 == 3 :
                print(visited)
                # print(stack2)
        return result
    
                             
    answer = 0
    for i in range(n) :
        for j in range(n) :
            if mt[i][j] == top_mt :
    
                result = dfs_mt(i, j)
                if answer < result :
                    answer = result

    print(f'#{t} {answer}')
    # print(mt == mt2)


#1 6
#2 3
#3 7
#4 4
#5 2
#6 12
#7 6
#8 7
#9 10
#10 19


# 8.15 visited 초기화를 시도했다. 완성 x
