import sys
sys.stdin = open('bj11286.txt', 'r')

import heapq


heap = []

N = int(input())

for i in range(N):
    num = int(input())

    if num == 0 :
        if heap == [] :
            answer = 0

        else :
            answer = heapq.heappop(heap)[1]
        print(answer)
    else :
        if num > 0 : 
            heapq.heappush(heap, (num, num))
        else :
            heapq.heappush(heap, (-num, num))
    
            