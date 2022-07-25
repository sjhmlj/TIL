import sys
sys.stdin = open('swea1206.txt', 'r')

for i in range(10) :
    width = input()
    height = list(map(int, input().split()))
    num = 0
    # print(height)
    for j in range(2, int(width)-2) :        # 0 ~ 99 /  0, 1, 98, 99 는 제외
        versus = max(height[j-1], height[j-2], height[j+1], height[j+2])
        if height[j] > versus :
            num += (height[j] - versus)
    print(f'#{i+1} {num}')

