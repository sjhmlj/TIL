import sys
sys.stdin = open('test.txt', 'r')

def pprint(x) :
    print('[-------------------------')
    for i in x :
        print('',i)
    print('-------------------------]')

move = {
    'R' : [0, 1],
    'L' : [0, -1],
    'B' : [1, 0],
    'T' : [-1, 0],
    'RT' : [-1, 1],
    'LT' : [-1, -1],
    'RB' : [1, 1],
    'LB' : [1, -1]
}
lc = {
    'A' : 1,
    'B' : 2,
    'C' : 3,
    'D' : 4,
    'E' : 5,
    'F' : 6,
    'G' : 7,
    'H' : 8
}


ch = [[0]* 8 for i in range(8)]


k, d, n = input().split()

ky = (8-int(k[1]))
kx = lc[k[0]]-1

dy = (8-int(d[1]))
dx = lc[d[0]]-1

ch[ky][kx] = 1               # 킹은 1
ch[dy][dx] = 2               # 돌은 2

# print(ky, kx)

for i in range(int(n)) :
    command = input()
    command = move[command]
    nky = ky + command[0]
    nkx = kx + command[1]
    # print(command, nky, nkx)

    if 0 <= nky <= 7 and 0 <= nkx <= 7 :
        if nky == dy and nkx == dx :

            if 0 <= dy + command[0] <= 7 and 0 <= dx + command[1] <= 7 :
                ch[dy][dx] = 0
                ch[dy+command[0]][dx+command[1]] = 2
                dy = dy+command[0]
                dx = dx+command[1]

                ch[ky][kx] = 0
                ch[nky][nkx] = 1
                ky = nky
                kx = nkx
            else :
                continue
        else :
            ch[ky][kx] = 0
            ch[nky][nkx] = 1
            ky = nky
            kx = nkx
            
    
kresult = ''
dresult = ''
for i in lc.items() :
    if i[1]-1 == kx :
        knum = i[0] 
    if i[1]-1 == dx :
        dnum = i[0]
kresult += str(knum) + str(8-ky)
dresult += str(dnum) + str(8-dy)


# pprint(ch)
# print(kx, dx)
print(kresult, dresult, sep = '\n')



## 백준 다른 사람 풀이
# import sys

# input = sys.stdin.readline

# info = {
#     "R": (0, 1),
#     "L": (0, -1),
#     "B": (1, 0),
#     "T": (-1, 0),
#     "RT": (-1, 1),
#     "LT": (-1, -1),
#     "RB": (1, 1),
#     "LB": (1, -1)
# }

# king, stone, n = input().split()
# kr, kc = 8-int(king[1]), ord(king[0])-ord("A")
# sr, sc = 8-int(stone[1]), ord(stone[0])-ord("A")
# for _ in range(int(n)):
#     cmd = input().strip()
#     dr, dc = info[cmd]
#     if not (0 <= kr+dr < 8 and 0 <= kc+dc < 8):
#         continue
#     kr += dr
#     kc += dc
#     if (kr, kc) == (sr, sc):
#         if not (0 <= sr+dr < 8 and 0 <= sc+dc < 8):
#         	# 킹의 움직임 되돌리기
#             kr -= dr
#             kc -= dc
#             continue
#         sr += dr
#         sc += dc
       
# print(chr(ord("A")+kc)+str(8-kr))
# print(chr(ord("A")+sc)+str(8-sr))