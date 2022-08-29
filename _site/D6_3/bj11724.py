import sys
sys.stdin = open('bj11724.txt', 'r')

n, m = list(map(int, input().split()))

def dfs(graph, start) :
    stack, visited = [], []

    stack.append(start)

    while stack :
        node = stack.pop()

        if node not in visited :
            visited.append(node)
            stack.extend(graph[node])
            

    return visited

edge = [list() for i in range(n+1)]

for i in range(m) :
    node1, node2 = list(map(int, input().split()))

    edge[node1].append(node2)
    edge[node2].append(node1)

connected = [0 for i in range(n+1)]      # 방문한 노드. visited를 이용해서 갱신할 것.
cnt = 0
for i in range(1, n+1) :
    if connected[i] == 0 :
        for j in dfs(edge, i) :
            connected[j] = 1

        cnt += 1
print(cnt)




#### 이런식으로도 되네                 백준 다른 사람 풀이. python 통과. 내껀 pypy
# import sys
# sys.setrecursionlimit(5000)
# input = sys.stdin.readline

# def dfs(pc):
#     visited[pc] = 1
#     for i in graph[pc]:
#         if visited[i] == 0:
#             dfs(i)

# N, M = map(int, input().split())
# N += 1

# graph = [[] for _ in range(N)]

# for _ in range(M):
#     v1, v2 = map(int, input().split())
#     graph[v1].append(v2)
#     graph[v2].append(v1)

# visited = [0] * N
# cnt = 0

# for j in range(1, N):
#     if not visited[j]:
#         if not graph[j]:
#             cnt += 1
#             visited[j] = 1
#         else:
#             dfs(j)
#             cnt += 1

# print(cnt)