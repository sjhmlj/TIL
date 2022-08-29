import sys

sys.stdin = open('swea14649.txt', 'r')

T = int(input())

for i in range(1, T+1) :
    num = list(map(int, input().split()))
    
    result = 0
    for j in range(len(num)) :
        if j % 2 == 0 :       ## 홀수자리
            result += num[j]*2

        else :
            result += num[j]
    result = result % 10
    result = (10 - result%10) if result %10 != 0 else 0
    print(f'#{i} {result}')