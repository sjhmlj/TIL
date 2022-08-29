import sys
sys.stdin = open('bj8958.txt', 'r')

T = int(input())
for i in range(1, T+1) :
    response = input()
    cnt = 0
    result = 0
    for j in response :           ## O가 연속으로 나오면 cnt가 계속 올라가고, X가 나오면 cnt는 0으로 초기화된다.
        if j == 'O' :
            cnt += 1
        else :
            cnt = 0
        result += cnt
    print(result)