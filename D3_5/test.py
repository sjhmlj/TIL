def f(n):
    x = 1
    while True:
        yield n*x
        x += 1

ot = f(2)
print(ot)
print(next(ot))
print(next(ot))
print(next(ot))