import sys
sys.stdin = open('bj2644.txt', 'r')

n = int(input())

p1, p2 = map(int, input().split())

e = int(input())
edge = [list()for i in range(n+1)]
for i in range(e) :
    n1, n2 = map(int, input().split())
    edge[n1].append(n2)
    edge[n2].append(n1)


def chonsu(start, end) :                  # 문제 접근 : 시작 노드부터 dfs로 하나씩 들어갈 때 cnt + 1, 
                                       #           다시 나올 때는 cnt -1
    visited = []
    stack = []
    stack.append(start) 
    cnt = 0                            # 촌수 구하기
    count = [0 for i in range(n+1)]    # 33번 줄을 위해서 만듬
    while True :
    
        node = stack.pop()
        count[node] += 1
        
        if node not in visited :          
            visited.append(node)
            stack.extend(edge[node]) 
            cnt += 1
        # elif node == start and count[node] <= len(edge[node]): 
        #     cnt -= 1
            
        elif count[node] < len(edge[node])  :  # 이 코드는 이미 방문한 정점이 node가 될 때(25줄) cnt -1이 되는 것을 방지하는 역할.
            cnt -= 1
        else : 
            pass
        print(node, cnt)
        if node == end :
            return cnt-1          # 첫 노드부터 cnt + 1이 되기 때문에 마지막에 1을 빼고 리턴
        if not stack :
            return(-1)
        

print(chonsu(p1, p2))



# 7
# 7 4
# 6
# 1 2
# 1 5
# 2 3
# 2 4
# 5 6
# 5 7

