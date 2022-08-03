import sys

sys.stdin = open('swea10804.txt', 'r')

T = int(input())

for i in range(T) :
    input_ = input()

    mirrdic = {
        'b' :'d', 
        'd' : 'b',
        'p' : 'q',
        'q' : 'p'
    }
    result = ''
    for a in input_ :
        result += mirrdic[a]
    print(f'#{i+1} {result[::-1]}')