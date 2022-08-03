import sys

sys.stdin = open('bj23825.txt', 'r')        

s, m = list(map(int, (input().split())))


result = min(s, m) // 2         ## s 와 m  둘 다 2개씩 쓰여야 하므로, 작은 개수의 블럭을 2로 나눈 몫이 최종 개수가 됨

print(result)

