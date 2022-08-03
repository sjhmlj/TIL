

import sys
sys.stdin = open('bj1269.txt', 'r')

n, m = input().split()

a = set(input().split())
b = set(input().split())

print(len(a^b))
