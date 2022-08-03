
import sys
sys.stdin = open('bj5063.txt', 'r')

N = int(input())
for i in range(N) :
    a, b, c = list(map(int, input().split()))


    income = b - a

    result = income - c

    if result > 0 :
        answer = 'advertise'

    elif result == 0 :
        answer = 'does not matter'

    else : 
        answer = 'do not advertise'
    print(answer)