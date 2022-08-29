import sys

sys.stdin = open("input_2050.txt", "r")

T = input()

for test_case in range(1, len(T) + 1):
    print(ord(T[test_case-1])-64, end = ' ')