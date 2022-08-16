import sys
sys.stdin = open('bj2606.txt', 'r')
from pprint import pprint
n = int(input())

e = int(input())

edge = [[] for i in range(n)]
stack = []
for i in range(e) :
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)
# pprint(edge)
stack.extend(edge[0])            # 처리해야할 노드를 표시
record = [0 for i in range(n)]
record[0] = 1                    # 방문한 노드를 표시
while True :
    if len(stack) == 0 :
        print('1번에서 멈춤')

        break

    while record[stack[-1]] == 1 :    # 이미 방문한 노드면 pop으로 제거
        stack.pop()
        # print(stack, record)
        if len(stack) == 0 : 
            # print('2번에서 멈춤')
            
            break

    if len(stack) == 0 : 
        # print('3번에서 멈춤')                
        break

    next = stack.pop()
    stack.extend(edge[next])
    record[next] = 1

    
print(record.count(1)-1)
# print(record)

# [[1, 4], [0, 2, 4], [1], [6], [0, 1, 5], [4], [3]]