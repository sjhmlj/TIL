# number = input()         # 내가 한 것. 이것도 그냥 number를 for 문에 돌리면 훨씬 간결하네. 

# sum1 = 0
# for i in range(len(number)) :
#     sum1 += int(number[i])

# print(sum1)          

# num 123                  ## 이런식으로 간결하게.
# sum1 = 0
# for i in str(num) :
#     sum1 += int(i)

# print(sum1)  

# number = 123           ## 한 줄로!

# print(sum(map( int,list(str(number)))))'

num = 123               ## 이런걸 바라셨음

result = 0
while num :
    result += num % 10
    num //= 10

print(result)
