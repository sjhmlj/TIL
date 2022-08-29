import sys

sys.stdin = open('zbj11652.txt', 'r') 

for i in range(2) :
    T = int(input())
    numdic = {}
    numlist = []

    for i in range(T) :
        a = int(input())
        numdic[a] = 0
        numlist.append(a)

    for i in numlist :
        numdic[i] += 1
    
    max_num = max(numdic.values())
    keylist = []
    for i in numdic.items() :
        if i[1] == max_num :
            keylist.append(i[0])

    keylist.sort()
    print(keylist[0])