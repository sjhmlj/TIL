from re import L
import sys

sys.stdin = open('bj2851.txt', 'r')       

for i in range(2) :

    result = 0
    numlist = []
    for i in range(10) :
        num = int(input())
        numlist.append(num)
    
    for i in range(10) :
        result += numlist[i]
        if result >= 100 :
            indexnum = i
            break
        elif i == 9 :                #! 이 경우를 생각 못했다. 
            indexnum = 10
    
    if indexnum != 0 and indexnum != 10 :
        resultmin = result - numlist[i]
        if (result -100) == (100 -resultmin) :
            print(result)
        else :
            if result-100 > 100 - resultmin :
                print(resultmin)
            else :
                print(result)

    else :
        print(result)
        