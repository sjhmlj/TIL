import sys
sys.stdin = open('bj9455.txt', 'r')
T = int(input())
for i in range(T) :
    m, n  = list(map(int, input().split()))

    grid = [list(map(int, input().split()))for i in range(m)]   # m행 n열

    boxnumlist = [0 for i in range(n)]
    for i in range(n) :                  # 각 열에 박스 개수를 세림. 뒤에 boxnum 변수를 사용하기 위해서. 
        for j in range(m) :
            if grid[j][i] == 1 :
                boxnumlist[i] += 1

    result = 0
    for i in range(n) :
        boxnum = boxnumlist[i]
        cnt = 0
        for j in range(m) :
            if grid[j][i] == 1 :          # 박스가 있으면, 맨 밑으로 내렸을 경우 이동해야 하는 개수를 구함
                boxnum -= 1               # 자기 자신 빼고
                cnt = (m-1) - (j) - (boxnum)   # 계산

                result += cnt

    print(result)


# T = int(input())             ## 백준 다른 사람 풀이
# for _ in range(T):
#     m, n = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(m)]
    
#     count = 0 
#     for j in range(n):
#         h = m-1
#         for i in range(m-1, -1, -1):
#             if arr[i][j] == 1:
#                 count += (h-i)
#                 h -= 1

#     print(count)