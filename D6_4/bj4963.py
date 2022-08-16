import sys
sys.stdin = open('test.txt', 'r')
from pprint import pprint
d8 = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
    [1, 1],
    [-1, 1],
    [1, -1],
    [-1, -1]
]
    

def dfs_island(s1, s2) :     # world 사용하자. 
    stack = [[s1, s2]]

    visited = [[0]*w for i in range(h)]
    visited[s1][s2] = 1

    while stack :
        n1, n2 = stack.pop()
        world[n1][n2] = 2
        
        for i in range(8) :
            nn1 = n1 + d8[i][0]
            nn2 = n2 + d8[i][1]

            if 0 <= nn1 <= h-1 and 0 <= nn2 <= w-1 :
                
                if world[nn1][nn2] == '1' :

                    if not visited[nn1][nn2] :

                        visited[nn1][nn2] = 1
                        stack.append([nn1, nn2])
                        world[nn1][nn2] = 2
                        

while True :
    w, h = map(int, input().split())

    if w + h == 0 :
        break
    
    world = []
    # print(world)
    for i in range(h) :
        world.append(input().split())
    # print(world)
    cnt = 0
    for i in range(h) :
        for j in range(w) :
            # print(i, j, h, w)
            # print(world)
            if world[i][j] == '1' :
                # print(1)
               
                dfs_island(i, j)
               

                cnt += 1

    print(cnt)



          

