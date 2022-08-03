import sys

sys.stdin = open('zbj1302.txt', 'r') 

for i in range(5) :
    T = int(input())
    bookdic = {}
    namelist = []
    for i in range(T) :
        name = input()
        bookdic[name] = 0
        namelist.append(name)
    for i in namelist :
        bookdic[i] += 1
    
    max_num = max(bookdic.values())
    
    sortedbook = list(bookdic.items())
    sortedbook.sort()
    for i in sortedbook :
        if i[1] == max_num :
            print(i[0])
            break

    # print( max_num)