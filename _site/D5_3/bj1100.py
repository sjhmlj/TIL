import sys
sys.stdin = open('bj1100.txt', 'r')

result = 0
for i in range(8) :
    a = list(input())
    cnt = 0
    # print(a)
    if i % 2 == 1 : 
        for j in range(1, 8, 2) :
            if a[j] == 'F' :
                cnt += 1
    else :
        for k in range(0, 7, 2) :
            if a[k] == 'F' :
                cnt += 1

    result += cnt

print(result)

