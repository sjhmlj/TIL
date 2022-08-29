from re import L
from pprint import pprint
import sys
sys.stdin = open('bj1236.txt', 'r')
for i in range(3) :
    n, m = list(map(int, input().split()))
    castle = []
    for i in range(n) :
        castle.append(list(input()))
    cntn = 0
    cntm = 0
    # pprint(castle)
    for i in range(n) :
        if 'X' not in castle[i] :
            cntn += 1

    for i in range(m) :
        check = 0
        for j in range(n) :
            if 'X' in castle[j][i] :
                check += 1
        if check == 0 :
            cntm += 1
    print(max(cntn, cntm))