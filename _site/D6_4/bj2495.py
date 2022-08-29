


for i in range(3) :
    num = input()
    cnt = 1
    result = 0
    for j in range(8-1) :
        elem = num[j] 
        if num[j+1] == elem :
            cnt += 1
        else :
            cnt = 1
        
        if cnt > result :
            result = cnt

    print(result)
        