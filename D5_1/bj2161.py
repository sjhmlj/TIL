import sys
sys.stdin = open('bj2161.txt', 'r')


N = int(input())
cardlist = []
for i in range(N) :
    cardlist.append(i+1)       # 1부터 N까지의 숫자를 리스트에 정렬
cnt = 0
result = []
while len(cardlist) :                  # 모든 카드를 제거할 때까지
    # num = cardlist[-1]
    if cnt % 2 == 0 :                  # cnt 변수를 이용해서 한번은 그냥 삭제, 한번은 뒤로 넣고 삭제를 실행함. 
        result.append(cardlist[0])
        cardlist.pop(0)
        
        
    else : 
        cardlist.append(cardlist[0])
        cardlist.pop(0)
    cnt += 1
        
    

    

print(*result)
    

### ----------

from collections import deque

N = int(input())

queue = deque(range(1, N+1))
result = []
while queue :
    result.append(queue.popleft())
    if queue :
        queue.append(queue.popleft())

print(result)
