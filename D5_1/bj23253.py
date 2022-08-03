# from re import L      


# import sys                                  
# sys.stdin = open('bj23253.txt', 'r')

# # totallist = []                       
# # N, M = list(map(int, input().split()))

# ## ---------------------------------------------------
# # for times in range(M) :                 #! 시간초과
# #     ip1 = input()            # 이건 안씀
# #     totallist.append(list(map(int, input().split())))

# # num = 1          # 책 정렬의 시작값 1         
# # check = True
# # for b in range(N) :
# #     for a in totallist :
# #         num2 = num
        
# #         if a != [] :
# #             if a[-1] == num : 
# #                 a.pop()
# #                 num += 1
# #                 break

# #         if a == totallist[-1] and num2 == num :
# #             check = False
# #     if check == False :
# #         break
        

# # if check == False :
# #     print('No')
# # else :
# #     print('Yes')


# ## ---------------------------------------------------

# # totallist = [[3, 1], [4, 2]]
# # totallist = [[3, 5, 1], [4, 2]]



# N, M = list(map(int, input().split()))      #!. 그냥 다른 방식으로 접근했어야 했다. 

# enlist = []
# indlist = []
# ip1 = 1
# for times in range(M) :               
#     ip1 += int(input())
#     enlist.append(list(map(int, input().split())))

# chan = True
# newlist = []
# num  = 1
# while chan :
#     for a in enlist :
#         if a !=[] :
#             if a[-1] == num :
#                 num += 1
                
#                 a.pop()
#                 break
        
#             elif a == enlist[-1] :
#                 # print('hi')
#                 chan = False
#     # print(num)
#     if num == N :
#         break
                
# if chan == True :
#     print('Yes')
# else :
#     print('No')



import sys                      #? 이게 정답이다. 다른 사람 코드를 보고 작성했다. 
input = sys.stdin.readline

N,M = list(map(int, input().split()))


result = True
for times in range(M) :               
    ip = int(input())
    dumlist = (list(map(int, input().split())))

    for j in range(ip-1) :
        if dumlist[j] < dumlist[j+1] :
            result = False
            break
    if result == False :
        break
if result == True :
    print('Yes')
else :
    print('No')


    