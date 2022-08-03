import sys

sys.stdin = open('swea10505.txt', 'r')


T = int(input())

for i in range(T) :
    num = int(input())

    moneylist = list(map(int, input().split()))

    result = 0

    for a in moneylist :
        result += a

    mean_ = result / num
    cnt = 0
    for b in moneylist :
        if b <= mean_ :
            cnt += 1

    print(f'#{i+1} {cnt}')