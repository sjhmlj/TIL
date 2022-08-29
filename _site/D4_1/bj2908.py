import sys
sys.stdin = open('bj2908.txt', 'r')

T = int(input())
for i in range(1, T+1) :
    a, b = list(input().split())
    a = a[::-1]
    b = b[::-1]
    print(max(a, b))
