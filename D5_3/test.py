n = 4
m = 3

a = [[0]* m for _ in range(n)]
b = [[0]* m ] * n

a[0][0] = 1
b[0][0] = 1

print(a)
print(b)