### 1번
# n = int(input())
# if n % 3 == 0 and n % 2 == 0 :
#     print('참')
# else :
#     print('거짓')

### 2번
# word = 'happy!'
# count = 0
# for i in word :
#     count += 1
# print(count)

###3번_1
# ip = int(input())
# n = 0
# s = 0
# while n< ip :
#     n += 1
#     s += n
# print(s)

###3번_2
# ip = int(input())
# s = 0
# for i in range(ip) :
#     s += i+1
# print(s)

###4번_1
# ip = int(input())
# n = 0
# x = 1
# while n< ip :
#     n += 1
#     x *= n
# print(x)

###4번_2
# ip = int(input())
# x = 1
# for i in range(ip) :
#     x *= (i+1)
# print(x)

###5번 
# numbers = [3, 10, 20]
# cnt = 0
# s = 0
# for i in numbers :
#     cnt += 1
#     s += i
    
# print(s//cnt)

###6번
# numbers = [0, 1, 0]
# l = numbers[0]
# for i in numbers :
#     if i >= l :
#         l = i
    
# print(l)

###7번
# numbers = [0, 20, 100]
# l = numbers[0]
# for i in numbers :
#     if i <= l :
#         l = i
    
# print(l)

###8번 두번째로 큰 수 구하기
numbers = [0, 20, 100]
l = numbers[0]
for i in numbers :
    if i >= l :
        l = i
numbers_2 = numbers
while l in numbers_2 :
    numbers_2.remove(l)  
l_2 = numbers_2[0]
for i in numbers :
    if i >= l_2 :
        l_2 = i
print(l_2)