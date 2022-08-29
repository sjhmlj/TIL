import sys
sys.stdin = open('bj2864.txt', 'r')

n, m = input().split()



max1 = n.replace('5', '6')
max2 = m.replace('5', '6')
min1 = n.replace('6', '5')
min2 = m.replace('6', '5')

print(int(min1)+int(min2), int(max1)+int(max2))




