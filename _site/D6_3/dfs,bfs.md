#### 개요
그래프 탐색
- dfs
- bfs

## DFS(Depth-First Search)
- 수직 방향으로 자료 검색 -> 하나씩 깊이 파고든다.
#### 구현 원리
- '앞으로 방문해야할 노드'와
- '이미 방문한 노드'를 기준으로 탐색. 
#### 구현 1. 스택/큐
- 리스트
```python
def dfs(graph, start_node) :
    need_visited, visited = list(), list()

    need_visited.append(start_node)

    while need_visited :
        node = need_visited.pop()

        if node not in visited :
            visited.append(node)
            need_visited.extend(graph[node])
    return visited
```

- deque
```python
def dfs2(graph, start_node) :
    from collections import deque

    need_visited, visited = deque(), list()

    need_visited.append(start_node)

    while need_visited :
        node = need_visited.popleft()

        if node not in visited :
            visited.append(node)
            need_visited.extend(graph[node])
    return visited
```
#### 구현 2. 재귀
```python
def dfs_recursive(graph, start, visited = []) :
    visited.append(start)

    for node in graph[start] :
        if node not in visited :
            dfs_recursive(graph, node, visited)
    return visited
```





## BFS(Breadth-First Search)
- 수평 방향으로 자료 검색
#### 구현 원리
- '방문하고자 하는 노드'와 
- '방문했던 노드'를 나누어서 알고리즘을 구성한다.
#### 구현
```python
def bfs(graph, start_node) :
    need_visited, visited = list(), list()

    # visited.append(start_node)
    need_visited.append(start_node)

    while need_visited :
        node = need_visited[0]
        del need_visited[0]

        if node not in visited :
            visited.append(node)
            # print(graph[node])
            need_visited.extend(graph[node])

    return visited
```
---
[데이터로 하는 마케팅](https://data-marketing-bk.tistory.com/entry/DFS-%EC%99%84%EB%B2%BD-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC?category=901221)

강의자료