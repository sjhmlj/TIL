import sys

sys.stdin = open("input_2071.txt", "r")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    input1 = input().split()
    sum1 = sum(map(int, input1))
    len_input = len(input1)
    mean1 = sum1/len_input

    print(f'#{test_case} {round(mean1)}')