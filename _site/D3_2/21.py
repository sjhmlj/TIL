


# number = 1234                   ## 내 풀이지만 참 조잡하다. 더 좋은 방법을 찾아보자. 
# number_len = number

# ## 자리수 구하기
# cnt = 0
# while number_len :
#     number_len //= 10
#     cnt += 1                 # 4

# new_num = 0
# for i in range(cnt-1, -1, -1) :
    
#     a = number // 10**i
#     number %= 10**i
#     new_num += a*10**(cnt-i-1)
#     print(a)
# print(new_num)

# number = 1234                ## 첫 번째 풀이에서 약간 개선
# number_len = number
# cnt = 0
# while number_len :
#     number_len //= 10
#     cnt += 1                 # 4

# new_num = 0
# while number :
#     new_num += number %10 * 10**(cnt -1)
#     cnt -= 1
#     number //= 10
    
    
# print(new_num)

# Number=1234                        ## 이태극님 풀이
# Reverse = 0

# while(Number > 0):
#     Reminder = Number %10
#     Reverse = (Reverse *10) + Reminder
#     Number = Number //10

# print(Reverse)


# num = 1234          ## 강사님 풀이. 깔끔하다. 
# result = 0

# while num :
#     result *= 10
#     result += num % 10

#     num //= 10
# print(result)

