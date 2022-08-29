import sys

sys.stdin = open("input_1976.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    a, b, c, d = list(map(int, input().split()))
    e = a + c 
    f = b + d
    if f >= 60 :
        f -= 60
        e += 1
    e = e if e <12 else e -12

    print(f'#{test_case} {e} {f}')
