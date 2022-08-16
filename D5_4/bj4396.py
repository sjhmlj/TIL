import sys
sys.stdin = open('bj4396.txt', 'r')

n = int(input())

fact = [list(input()) for i in range(n)]

answer = [list(input()) for i in range(n)]

result = [['.']*n for i in range(n)]
star = '*'
# for i in range(n) :
#     for j in range(n) :
#         cnt = 0
#         if fact[i][j] != star :
#             if i != 0 and j != 0 :
#                 cnt += fact[i-1][j-1 :j+2].count(star)
#                 cnt += fact[i][j-1].count(star)
#                 cnt += fact[i][j+1].count(star)
#                 cnt += fact[i+1][j-1 :j+2].count(star)
#             elif i == 0 and j != 0 :
#                 cnt += fact[i][j-1].count(star)
#                 cnt += fact[i][j+1].count(star)
#                 cnt += fact[i+1][j-1 :j+2].count(star)
#             elif i != 0  and j == 0 :
#                 cnt += fact[i-1][j:j+2].count(star)
#                 cnt += fact[i][j+1].count(star)
#                 cnt += fact[i+1][j:j+2].count(star)
#             elif i == 0  and j == 0 :
#                 cnt += fact[i][j+1].count(star)


fact2 = [[0]*(n+2) for i in range(n+2)]

for i in range(n) :
    for j in range(n) :
        if fact[i][j] == star :
            fact2[i+1][j+1] = star
# print(fact2)

for i in range(n) :
    for j in range(n) :
        cnt = 0
        if fact2[i+1][j+1] != star :
            cnt += fact2[i][j :j+3].count(star)
            cnt += 1 if fact2[i+1][j] == star else 0
            cnt += 1 if fact2[i+1][j+2] == star else 0
            cnt += fact2[i+2][j :j+3].count(star)

            result[i][j] = cnt
        else :
            result[i][j] = star
its = True
for i in range(n) :
    for j in range(n) :
        if answer[i][j] == 'x' :
            answer[i][j] = result[i][j]
            if answer[i][j] == star :
                its = False
                

if its == True :
    for i in answer :
        for j in i :
            print(j, end = '')
        print()
# else :                           # 이 답을 원하는게 아닌가보다. 
#     for i in fact :
#         for j in i :
#             print(j, end = '')
#         print()
else :
    for i in range(n) :
        for j in range(n) :
            if fact[i][j] == star :
                print(star, end= '')
            else :
                print(answer[i][j], end= '')

        print()

