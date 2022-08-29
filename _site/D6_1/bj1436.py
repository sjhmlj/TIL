N = int(input())

result = []
for i in range(3660000) :
    if '666' in str(i) :
        result.append(i)
# print(result)
print(result[N-1])
print(len(result))               ## 3660000 일 때 12894