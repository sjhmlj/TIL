

mt = [[9, 3, 2, 3, 2], [6, 3, 1, 7, 5], [3, 4, 8, 9, 9], [2, 3, 7, 7, 7], [7, 6, 5, 5, 8]]

n = 5
k = 2

top_mt = 9

dxy = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

def dfs_mt(node1, node2) :
    
    result = 1
    visited = [[0]*n for i in range(n)]
    for clap in range(1, top_mt+1) :
        stack = [[node1, node2, 1]]
        stack2 = []
        # if node2 == 3 :
        #     print(visited)
        while stack :
            # if len(stack) >= 2 :         # 스택2를 모조리 빼줘야 한다. 여기 조건이 그걸 충족하지 못하고 있다. 

            #     if stack[-1][2] > stack[-2][2] :
            #         y2, x2, cnt2 = stack2.pop()
            #         visited[y2][x2] = 0

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
                            
            # 초기화 단계
            if cnt-1 == clap :
                mt[y][x] += k

            if len_stack == len(stack) :       # 각 경로의 끝에 도달했을 때 실행됨
                visited[y][x] = 0
                while True :
                    if stack  :
                        if cnt > stack[-1][2] :
                            # print('STOP', stack[-1], stack2[-1])
                            y2, x2, cnt = stack2.pop()
                            visited[y2][x2] = 0
                        else :
                            break
                    else : 
                        break

                        

                
            else :
                stack2.append([y, x, cnt])
        while stack2 :
            y2, x2, cnt2 = stack2.pop()
            visited[y2][x2] = 0
            

        # if node2 == 3 :
        #     # print(y, x, mt[y][x], cnt, clap)

        #     print(stack2)
            # pprint(stack)
        if result < clap :
            return result
        # if node2 == 3 :
        #     print(visited)
            # print(stack2)
    return result

                            
answer = 0
for i in range(n) :
    for j in range(n) :
        if mt[i][j] == top_mt :

            result = dfs_mt(i, j)
            if answer < result :
                answer = result

print(f'{answer}')
