import sys
sys.stdin =  open('swea5431.txt', 'r')

T = int(input())
for t in range(1, T+1) :
    n, k = list(map(int, input().split()))
    studentlist = list(map(int, input().split()))
    nolist = []
    for i in range(1, n+1) :
        if i in studentlist :
            continue
        else :
            nolist.append(i)

    print(f'#{t}', end = ' ')
    print(*nolist)


