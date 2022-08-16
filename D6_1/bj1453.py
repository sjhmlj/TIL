import sys
sys.stdin = open('bj1453.txt', 'r')

n = int(input())

seat = list(input().split())
print(seat, len(seat))
print(n - len(set(seat)))