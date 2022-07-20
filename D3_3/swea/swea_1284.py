import sys

sys.stdin = open("input_1284.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    list1 = map(int, input().split())
    p, q, r, s, w = list1
    a_cost = p*w
    b_cost = q if w <= r else q + (w-r)*s
    print(f'#{test_case} {min(a_cost, b_cost)}')