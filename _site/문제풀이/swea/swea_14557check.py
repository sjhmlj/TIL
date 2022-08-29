from re import L
import sys

sys.stdin = open("input_14557.txt", "r")

T = int(input())

# for test_case in range(1, T + 1):      # ! 첫번째 시도, 그냥 안돌아감
#     ip_list = list(map(int, list(input())))
#     cnt = 0
#     while cnt < len(ip_list) :           ## 총 요소개수만큼 돌려보자. 
#         cnt += 1
#         # print(cnt, end= ' ')         # ok 1 2 3 1 2 3 4 1 2 3 4 5
#         for i in range(len(ip_list)):   
#             # print(type(ip_list[i]))
#             if ip_list[i] == 1 :      # ! 이 코드로 접근이 안되네. --> 요소가 'str'이네???  -> 해결
#                 print(i)
#                 if i == 0 :
                    
#                     if len(ip_list) != 1 :
#                         ip_list[i+1] = 0 if ip_list[i+1] == 1 else 1
#                     ip_list.pop(i)
#                     break    
#                 else : 
#                     if (i+1) != len(ip_list) :
#                         print(i)
#                         ip_list[i-1] = 0 if ip_list[i-1] == 1 else 1
#                         ip_list[i+1] = 0 if ip_list[i+1] == 1 else 1
#                         ip_list.pop(i)
#                         break
#                     else : 
#                         ip_list[i-1] = 0 if ip_list[i-1] == 1 else 1
#                         ip_list.pop(i)
#                         break


#     print(ip_list)
            
# for test_case in range(1, T + 1):        #! 두 번째 시도, 터미널에서 답은 나옴 but 제한시간 초과로 인한 실패. 
#     ip_list = list(map(int, list(input())))
#     cnt = 0
#     while cnt < len(ip_list) :          ## 뒤에를 제거하고 앞의 카드를 제거하는 경우가 있어서. 
#         cnt += 1
#         for i in range(len(ip_list)) :
#             if ip_list[i] == 1 :
#                 if i == 0 : 
#                     ip_list[i] = 2
#                     if len(ip_list) != (i+1) :       # i+1 인덱스가 존재할 때
#                         if ip_list[i+1] == 0 : 
#                             ip_list[i+1] = 1
#                         elif ip_list[i+1] == 1 :
#                             ip_list[i+1] = 0
                    
#                 elif len(ip_list) ==(i+1) :
#                     ip_list[i] = 2
#                     if ip_list[i-1] == 0 : 
#                         ip_list[i-1] = 1
#                     elif ip_list[i-1] == 1 :
#                         ip_list[i-1] = 0
#                 else :
#                     ip_list[i] = 2
#                     if ip_list[i-1] == 0 : 
#                         ip_list[i-1] = 1
#                     elif ip_list[i-1] == 1 :
#                         ip_list[i-1] = 0
#                     if ip_list[i+1] == 0 : 
#                         ip_list[i+1] = 1
#                     elif ip_list[i+1] == 1 :
#                         ip_list[i+1] = 0
#     # print(ip_list)           # ok
#     result = 'yes' if 0 not in ip_list else 'no'
#     print(f'#{test_case} {result}')

def index_exist (list, i) :             #? 통과하긴 했는데, 다른 사람들에 비해 메모리가 압도적으로 높다. 실행시간도, 코드 길이도. 
    return (0<= i< len(list))  # (-len(list) <= i < 0)

for test_case in range(1, T + 1) :
    ip = list(input())
    while '1' in ip :
        for i in range(len(ip)) :
            
            if ip[i] == '1' :
                ip[i] = 2 
                
                if index_exist(ip, i+1) :
                    if ip[i+1] == '0' :
                        ip[i+1] = '1'
                    elif ip[i+1] == '1' :
                        ip[i+1] = '0'
                
                if index_exist(ip, i-1) :
                    if ip[i-1] == '0' :
                        ip[i-1] = '1'
                    elif ip[i-1] == '1' :
                        ip[i-1] = '0'
            # print(ip)
    result = 'no' if '0' in ip else 'yes'
    print(f'#{test_case} {result}')




# for test_case in range(1, T +1):            #? 핵심이다. 이런 통찰력이 코드를 줄여주네
#     a = 'yes' if input().count('1') % 2 == 1 else 'no'
#     print(f'#{test_case} {a}')