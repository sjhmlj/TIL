import sys

sys.stdin = open("input_2019.txt", "r")

T = int(input())

for test_case in range(0, T + 1):
    print(2**test_case, end = ' ')