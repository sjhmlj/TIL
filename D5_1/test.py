from collections import deque

N = int(input())

queue = deque(range(1, N+1))
result = []
while queue :
    result.append(queue.popleft())
    if queue :
        queue.append(queue.popleft())

print(result)

