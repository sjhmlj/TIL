from re import L
import sys
sys.stdin = open('bj2167.txt', 'r')

# n, m = list(map(int, input().split()))         #! 문제 이해를 잘못했다. 그래도 좋은 코드 짠 것 같다.

# list2 = []
# for i in range(n) :
#     a = list(map(int, input().split()))

#     list2.append(a)

# k = int(input())

# for i in range(k) :
#     a, b, c, d = list(map(int, input().split()))
#     result = 0
#     if a == c :
#         for j in range(b-1, d) :
#             result += list2[a-1][j]
#     else :
#         for e in range(a-1, c) :
#             if e == a-1 :

#                 for f in range(b-1, m) :
#                     result += list2[e][f]
#             elif e == c :
#                 for g in range(d) :
#                     result += list2[e][g]

#             else : 
#                 for h in range(m) :
#                     result += list2[e][h]
#     print(result)



n, m = list(map(int, input().split()))         

list2 = []
for i in range(n) :
    a = list(map(int, input().split()))

    list2.append(a)                   ## n x m 행렬

k = int(input())

for i in range(k) :
    a, b, c, d = list(map(int, input().split()))
    result = 0
    
    for e in range(a-1, c) :       ## 드래그 형식의 합이라서 
        for f in range(b-1, d) :   ## 이런식으로 작동.    행 인덱스 사이의 값과 열 인덱스 사이의 값. 
            result += list2[e][f]

    print(result)





# # 배열의 크기 입력                        # 백준에서 시간 짧게 나온 코드를 가져왔다. 코드만 보니까 이해가 안가네
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]

# # 부분의 개수 입력
# K = int(input())
# dp = [[0] * (M+1) for _ in range(N+1)]

# for i in range(1, N+1):
#     for j in range(1, M+1):
#         dp[i][j] = arr[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

# for _ in range(K):
#     i, j, x, y = map(int, input().split())
#     print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])


