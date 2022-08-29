import sys
sys.stdin = open('bj2606.txt', 'r')

n = int(input())
m = int(input())

edge = [list() for i in range(n+1)]
for i in range(m) :
    a, b = list(map(int, input().split()))

    edge[a].append(b)
    edge[b].append(a)


def dfs(graph, start) :

    stack, visited = [], []
    stack.append(start)
    while stack :
        node = stack.pop()
        if node not in visited :
            visited.append(node)
            stack.extend(graph[node])

    return visited

print(len(dfs(edge, 1))-1)
    