import sys

sys.stdin = open('bj1157.txt', 'r')              

                                   #! 두 경우 다 실행시간이 너무 길다. 두 번째꺼는 시간 초과로 제출이 안된다. 
for i in range(4) :
    input_ = input()
    ordlist = []
    for i in input_ :
        ord_ = ord(i)
        if ord_ > 96 :
            ord_ = ord(i) - 32
        ordlist.append(ord_)
    # print(ordlist)
    
    ordset = set(ordlist)
    # print(ordset)
    max_ordlist = []
    maxnum = 0
    for i in ordset :
        if ordlist.count(i) > maxnum :
            maxnum = ordlist.count(i)
    for i in ordset :
        if ordlist.count(i) == maxnum :
            max_ordlist.append(i)
            
        

    # print(max_ordlist, 1)

    if len(max_ordlist) == 1:
        print(chr(max_ordlist[0]))
    else :
        print('?')



    ordnumlist = []                 #! 2. 시간 초과.
    maxcountnum = 0
    for i in ordlist :
        if ordlist.count(i) > maxcountnum :
            maxcountnum = ordlist.count(i)
            ordnumlist = [i]
        if ordlist.count(i) == maxcountnum :
            ordnumlist.append(i)
    # print(ordnumlist)

    if len(set(ordnumlist)) == 1 :
        print(chr(ordnumlist[0]))
    else :
        print('?')
        


    
