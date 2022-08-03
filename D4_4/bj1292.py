from re import L
import sys

sys.stdin = open('bj1292.txt', 'r')  

a, b = list(map(int, input().split()))
result = 0

for i in range(a, b+1) :
    sum_ = 0
    for j in range(b+1) :             ## 어떤 인덱스의 숫자를 알려면 1+2+3+ ...를 더한 값과 인덱스값을 비교하면 된다. 
        sum_ += j                    ## 예를 들어 3번째 숫자는 1+2 >= 3 이므로 3이되고, 4번째 숫자는 1+2+3 >= 4 이므로 3이 된다. 
        # print(sum_, i, end= '//')
        if sum_ >= i :
            num = j
            break
    result += num
    
print(result)


