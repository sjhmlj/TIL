from re import I
import sys

sys.stdin = open("input_1986.txt", "r")

T = int(input())
result = 0
for test_case in range(1, T + 1):
    if test_case % 2 == 0 :
        result -= test_case
    else : 
        result += test_case
    print(f'#{test_case} {result}')
