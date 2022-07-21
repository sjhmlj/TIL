# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# str1 =''
# for test_case in range(1, T + 2):
#     a = 9 - test_case
#     str1 += str(a)
#     str1 += ' '
# print(str1)

# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# str1 =''
# for test_case in range(1, T + 2):
#     a = 9 - test_case
#     str1 += str(a)
#     if a != 0 :
#         str1 += ' '

# print(str1)

# T = int(input())

# for test_case in range(1, T + 2):
#     a = 9-test_case
#     if a != 0 :
#         print(a, end= ' ')
#     else : 
#         print(a)


# T = int(input())

# for test_case in range(1, T + 1):
#     a = 9-test_case
#     if a != 1 :
#         print(a, end= ' ')
#     else : 
#         print(a, 0, sep=' ')

T = int(input())

for test_case in range(T, -1, -1):
    if test_case != 0 :
        print(test_case, end = ' ')
    else : 
        print(test_case)