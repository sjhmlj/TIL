import sys

sys.stdin = open('swea14654.txt', 'r')


T = int(input())

for k in range(T) :
    input_ = input()

    startnum = ['3', '4','5', '6', '9']
    ox = False
    if input_[0] in startnum:
        ox = True
    
    
    cnt = 0
    for i in input_ :
        if i != '-' :
            cnt += 1

    if ox == True and cnt == 16 :
        result = 1
    else :
        result = 0

    print(f'#{k+1} {result}')