import sys
sys.stdin = open('bj2669.txt', 'r')

xy = [[0]* 100 for i in range(100)]              ## 입력이 100x100이 최대여서 행렬을 만들었다.

input_ = [list(map(int, input().split())) for i in range(4)]

for i in input_ :                              ## 넓이를 구하는 걸, 1x1 격자 안의 숫자를 세는걸로 대체할 거다.
    for j in range(i[0], i[2]) :
        for k in range(i[1], i[3]) :
            xy[j][k]= 1
cnt = 0
for line in xy :
    cnt += line.count(1)

print(cnt)



### 백동원님 풀이
### 백동원
# from collections import deque

# squares = deque([list(map(int, input().split())) for _ in range(4)])
# 총넓이 = 0
# X = 0
# for 사각형 in squares:
#     총넓이 += (사각형[2] - 사각형[0]) * (사각형[3]- 사각형[1])
# for a in squares:
#     for b in squares:
#         if (max(a[0], b[0]) < min(a[2], b[2])) and (max(a[1], b[1]) < min(a[3], b[3])):
#             X += (min(a[2], b[2]) - max(a[0], b[0])) * (min(a[3], b[3]) - max(a[1], b[1]))

# for 사각형 in squares:
#     X -= (사각형[2] - 사각형[0]) * (사각형[3]- 사각형[1])
# X /= 2
# 총넓이 -= int(X)

# for c in range(4):
#     list_ = squares.popleft()
#     if (max(squares[0][0], squares[1][0], squares[2][0]) < min(squares[0][2], squares[1][2], squares[2][2])) and (max(squares[0][1], squares[1][1], squares[2][1]) < min(squares[0][3], squares[1][3], squares[2][3])):
#         총넓이 += (min(squares[0][2], squares[1][2], squares[2][2]) - max(squares[0][0], squares[1][0], squares[2][0])) * (min(squares[0][3], squares[1][3], squares[2][3]) - max(squares[0][1], squares[1][1], squares[2][1]))
#     squares.append(list_)

# A = []
# B = []
# C = []
# D = []
# for _ in squares:
#     A.append(_[0])
#     B.append(_[2])
#     C.append(_[1])
#     D.append(_[3])
# if (max(A) < min(B)) and (max(C) < min(D)):
#     총넓이 -= (min(B) - max(A)) * (min(D) - max(C))
# print(총넓이)