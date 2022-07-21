import sys

sys.stdin = open("input_1989.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    word1 = input()
    word2 = word1[::-1]

    print(f'#{test_case} {1 if word1 == word2 else 0}')