import sys

sys.stdin = open("input_1926.txt", "r")

# T = int(input())

# for test_case in range(1, T + 1):      ## -- 를 표현 못함. 
#     if '3' in str(test_case) :
#         for j in str(test_case) :
#             if j in '369' :
#                 print('-', end = ' ')
#     elif '6' in str(test_case) :
#         for j in str(test_case) :
#             if j in '369' :
#                 print('-', end = ' ')
#     elif '9' in str(test_case) :
#         for j in str(test_case) :
#             if j in '369' :
#                 print('-', end = ' ')
#     else :
#         print(test_case, end= ' ')
    

T = int(input())

for test_case in range(1, T + 1):
    num = str(test_case)
    cnt = 0
    for i in num :
        if i in '369' :
            cnt += 1

    
    if cnt == 1 :
        print('-', end = ' ')
    elif cnt == 2 :
        print('--', end = ' ')
    elif cnt == 3 :
        print('---', end = ' ')
    else :
        print(num, end = ' ')
            
    # if cnt == 0 :                        # 이게 더 깔끔!!
    #     print(num, end = ' ')
    # else :
    #     print('-'*cnt, end = ' ')