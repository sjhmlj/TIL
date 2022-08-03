import sys
sys.stdin = open('bj15953.txt', 'r')

N = int(input())

adic = {
    1 : 500,
    2 : 300,
    3 : 200,
    4 : 50, 
    5 : 30,
    6 : 10
}
bdic = {
    1 : 512,
    2 : 256,
    3 : 128,
    4 : 64, 
    5 : 32
}


for i in range(N) :
    a, b = list(map(int, input().split()))

    result = 0

    cnt1 = 0
    for i in range(1, 7) :
        cnt1 += i
        if a <= cnt1 :
            result += adic[i]
            break
    cnt2 = 0
    for i in range(1, 6) :
        cnt2 += 2**(i-1)
        if b <= cnt2 :
            result += bdic[i]
            break
    print(result*10000)




