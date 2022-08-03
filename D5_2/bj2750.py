import sys

sys.stdin = open('bj2750.txt', 'r')

N = int(input())
list_ = []
for i in range(N) :
    list_.append(int(input()))

list_.sort()

for j in list_ :
    print(j)