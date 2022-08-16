import sys
sys.stdin = open('bj2798.txt', 'r')

n, m = list(map(int, input().split()))

card = list(map(int, input().split()))
result = 0
for i in range(n-2) :
    for j in range(i+1, n-1) :
        for k in range(j+1, n) :
            num = card[i] + card[j] + card[k]

            if num > result and num < m+1 :
                result = num

print(result)