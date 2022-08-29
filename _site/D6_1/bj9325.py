T = int(input())
for t in range(T) :
    s = int(input())
    b = int(input())
    result = s
    for i in range(b) :
        q, p = list(map(int, input().split()))
        result += q* p
    print(result)

