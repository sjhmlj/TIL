# def add(a, b) :
#     return a + b

# def minus(a, b) :
#     return a - b

# print(add(5, 10))
# print(minus(5, 10))


# a = print('hi', 'hello', sep = '', end = '')  
# print(1)

# def my_add(*numbers) :
#     return numbers
# result = my_add(1, 2, 3)
# print(result, type(result))

# from operator import ne


# numbers = ['1','2', '3']
# # new_numbers = []
# # for i in numbers :
# #     new_numbers.append(int(i))
# # print(new_numbers)

# new_numbers_2 = map(int, numbers)
# print(new_numbers_2)  ## 이미 함수가 모두 적용됨. 

# n, m = map(int, input().split())
# print(n*m)

# def afa(1) :   ## '' 에러남 1 에러남 [] 에러남
#     return 1  

# print(afa(3))

# def add(*arg) :
#     return arg
# def add_2(**kwarg):
#     return kwarg
# result_1= add([1, 2, 3])
# result_2= add_2(jh = 120, jt = '100')
# print(result_1, result_2, sep ='///')

# def foo(arg) :
#     return arg
# result = foo([1, 2, 3])
# print(result)


# a = 3
# def add(x, y) :
#     a = 2
#     return x+ y+ a
# print(add(0,0))
# print(a)

#------------------------------------##
#예제 1번
# ip = int(input())
# def cube(n) :
#     return n**3

# print(cube(ip))

#예제 2번
# a = int(input('가로'))
# b = int(input('세로'))

# def rectangle(a, b) :
#     return a*b, (a +b)*2

# print(rectangle(a, b))

#9번
# students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']
# cnt = 0
# for i in students :
#     if i == '이영희' :
#         cnt += 1
# print(cnt)
# while '이영희' in students : 
#     students.remove('이영희')
#     cnt += 1
# print(cnt)

#10번
# numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]
# cnt = 0
# for i in numbers :
#     if i == 5 :
#         cnt += 1
# print(cnt)

# cnt = 0
# for i in range(len(numbers)) : 
#     if numbers[i] == 5 :
#         cnt += 1
# print(cnt)

#11번

# for i in range(1,10) :
#     print(f'{i}단 ')
#     for j in range(1,10) :
#         print(f'{i} x {j} = {i*j}')
    
# print(f'{{'{{'{4}'}}'}}')   # 에러

##12번
# word = list(input())   ### 이거는 실패
# for i in word :
#     if i == 'a' :
#         word.remove(i)
# for i in range(len(word)) :
    
# word_2 = map(str, word)
# print(word_2)
# word = input()
# for i in word :
#     if i == 'a' : 
#         continue
#     else : 
#         print(i, end='')

# print()     # %를 없애기 위해서 씀

##13번
# word = input()
# for i in range(len(word)-1,-1,-1) :
#     print(word[i], end = (''))
# print()

# word = input()
# a = word[::-1]
# print(a)

# word = 'hello'
# word += '!'   #  이건 됨
# print(word)
# word -= '!'    # 이건 안됨


# print(True and 0)
result = 1 and '값은 0이 아닙니다'


print(result)