
# ## 리스트 메서드 활용
# a = [10, 1, 100]
# new_a = a.sort()
# print(a, new_a)
# # [1, 20, 100] None
# # 리스트 메서드를 활용하면, 그 메서드를 정렬된 상태로 변경(원본 변경)
# # return 되는 것은 None

# ## 리스트에 sorted 함수를 활용
# b = a
# new_b = sorted(b)
# print(b, new_b)
# # [10, 1, 100] [1, 10, 100]

# a = 'h i'
# b, c = a.split()
# print(type(b))

#14번
# word = input()
# cnt = 0
# for i in word :
#     if i == 'a' :
#         cnt += 1
# print(cnt)

#15번
# word = input()
# cnt = -1
# for i in word :
#     cnt += 1
#     if i == 'a' :
#         cnt += 1
#         print(cnt-1)
#         break
    
# if cnt == len(word)-1 :
#     print(-1)

#16번
# word = input()
# cnt = 0
# for i in word :
#     if i == 'a' :
#         cnt += 1
#     elif i == 'e' :
#         cnt += 1
#     elif i == 'i' :
#         cnt += 1
#     elif i == 'o' :
#         cnt += 1
#     elif i == 'u' :
#         cnt += 1
# print(cnt)

# word = input()
# cnt = 0
# for i in word :
#     if i == 'a' or 'e' or 'i' or 'o' or 'u':   ## 제대로 안된다. 그냥 다 카운트 해버린다. 
#         cnt += 1
    
# print(cnt)

## 17번
# word = list(input())         ## 그냥 스트링으로 진행하면 훨씬 깔끔한 코드가 나오네
# word_new =''
# for i in range(len(word)) :
    
#     word_new += chr(ord(str(word[i]))-32)   
# print(word_new)

#18번
# word = input()
# dic = {}
# cnt = 0
# for i in word :
#     cnt_i = 0         ## 이런식으로 작동하지 않는다. 
#     print(i)
#     # print(i)


# for i in word :
#     dic[i] = 0

# for i in word :
#     dic[i] += 1

# # word_new = sorted(set(word))

# for i in dic :
#     print(i, dic[i])


