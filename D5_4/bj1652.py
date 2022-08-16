
import sys
sys.stdin = open('bj1652.txt', 'r')

n = int(input())
room = [list(input())for i in range(n)]
# print(room)

cntr = 0
cntc = 0

for i in range(n) :
    its = True
    for j in range(n-1) :
        if its == True and room [i][j] =='.' and room[i][j+1] == '.' :
            cntc += 1
            its = False
        elif room[i][j] != '.' :
            its = True
    its = True
    for k in range(n-1) :
        if its == True and room [k][i] =='.' and room[k+1][i] == '.' :
            cntr += 1
            its = False
        elif room[k][i] != '.' :
            its = True
print(cntc, cntr)