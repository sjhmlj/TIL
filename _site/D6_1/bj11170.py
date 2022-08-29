T = int(input())

for t in range(T) :
    a, b = list(map(int, input().split()))
    result = 0
    for i in range(a, b+1) :
        result += str(i).count('0')

    print(result)
    