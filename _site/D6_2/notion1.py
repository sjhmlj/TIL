import sys
sys.stdin = open('notion1.txt', 'r')

from pprint import pprint

n, m = 7, 6

ad_m = [[0]*n for i in range(n)]
ad_l = [[] for i in range(n)]
# pprint(ad_l)
# pprint(ad_m)
for i in range(m) :
    a, b = list(map(int, input().split()))

    ad_m[a][b] = 1
    ad_m[b][a] = 1
    

    ad_l[a].append(b)
    ad_l[b].append(a)

pprint(ad_m)
pprint(ad_l)