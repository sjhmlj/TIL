word = input()
dic = {}
for i in word :
    dic[i] = 0

for i in word :
    dic[i] += 1


for i in dic :
    print(i, dic[i])
