import sys

sys.stdin = open('zbj1764.txt', 'r') 

nhnsname = {}
noseename = []
nohearname = []
a, b = list(map(int, input().split()))

for i in range(a) :
    name = input()
    nhnsname[name] = 0
    nohearname.append(name)
for i in range(b) :
    name = input()
    nhnsname[name] = 0
    noseename.append(name)

for i in noseename :
    nhnsname[i] += 1
for i in nohearname :
    nhnsname[i] += 1

r_nhnsname = []
for i in nhnsname.items():
    if i[1] == 2 :
        r_nhnsname.append(i[0])

r_nhnsname.sort()

print(len(r_nhnsname))
for i in r_nhnsname :
    print(i)



