#### 개요
- 완전탐색(Exhaustive Search)
  - brute-force
  - delta-search

## brute-force
- 모든 경우의 수를 탐색하여 문제를 해결하는 방식이다. 

## delta search
- 이차원 리스트의 인덱스 조작을 통해서 상하좌우 탐색을 한다.이때 행과 열의 변량인 -1, +1을 델타 값이라고 한다.
```python
dx = [-1, -1, 0, 0]
dy = [-0, -0, -1, 1]

for x in range(n) :
  for y in range(m) :
    for i in range(4) :
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m :
        x = nx
        y = ny
```
