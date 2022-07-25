from re import L
import sys
sys.stdin = open('swea1208.txt', 'r')

for i in range(10) :
    times = int(input())           # 덤프 시행 횟수
    height = list(map(int, input().split()))    ## 100개짜리 int 리스트
    for r in range(times) :
        high_height = max(height)
        low_height = min(height)
        for j in range(len(height)) :
            if height[j] == high_height :
                height[j] -= 1
                break
               
        for k in range(len(height)) :
            if height[k] == low_height :
                height[k] += 1
                break
                
    print(f'#{i+1} {max(height) - min(height)}')
        