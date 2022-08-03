from re import L
import sys

sys.stdin = open('swea1228.txt', 'r')

for k in range(10) :

    one = int(input())
    two = input().split()
    three = int(input())
    four = input().split()

    result = two

    for i in range(len(four)) :
        if four[i] == 'I' :
            # num = i
            # numforindex = 0
            # for j in range(int(four[i+2])) :
            #     result.insert(int(four[i+1])+numforindex, four[num+3])
            #     # print(four[num+3])
            #     num += 1
            #     numforindex += 1
            
            ## 런타임 에러가 떠서 이 부분을 수정해봐야 할 것 같다. 이유는 모르겠다.
            num = 1
            index_ = i+1
            num2 = 0
            continue
        
        if num >= 3 :
            result.insert(int(four[index_]) + num2, four[i])
            num2 += 1
            # print(index_)
            # print(result)
            # break
        num += 1
        # print(result[:10])
    
    
    # break
    print(f'#{k+1}', end = ' ')
    for i in range(10) :
        print(result[i], end = ' ')    
    print()
    
    # for i in range(len(four)) :
    #     if four[i] == 'I' :
    #         num = i
    #         numforindex = 0
    #         for j in range(int(four[i+2])) :
    #             result.insert(int(four[i+1])+numforindex, four[num+3])
    #             # print(four[num+3])
    #             num += 1
    #             numforindex += 1
            
    #         ## 런타임 에러가 떠서 이 부분을 수정해봐야 할 것 같다. 이유는 모르겠다.

    #     else : 
    #         continue