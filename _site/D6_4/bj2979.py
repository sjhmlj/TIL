import sys
sys.stdin = open('test.txt', 'r')

a, b, c = map(int, input().split())

start_l = []
end_l = []

for i in range(3) :
    start, end = map(int, input().split())
    start_l.append(start)
    end_l.append(end)

timeline = [0 for i in range(max(end_l) +1)]

for i in range(3) :
    for j in range(start_l[i]+1, end_l[i]+1) :
        timeline[j] += 1

# print(timeline)

result = 0
for i in timeline :
    if i == 0 :
        pass
    elif i == 1 :
        result += i* a
    elif i == 2 :
        result += i* b
    else :
        result += i *c

print(result)

