import sys
sys.stdin = open('bj2309.txt', 'r')
nanjang = []

for i in range(9) :                    # 난쟁이 9명
    nanjang.append(int(input()))

num = sum(nanjang) - 100              

for i in range(8) :
    for j in range(i+1, 9) :
        if nanjang[i]+ nanjang[j] == num :
            impo1 = nanjang[i]
            impo2 = nanjang[j]

nanjang.remove(impo1)
nanjang.remove(impo2)
# print(index_)
nanjang.sort()

for i in range(7) :
    print(nanjang[i])              

# print(sum(nanjang))