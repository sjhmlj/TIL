from re import L
import sys

sys.stdin = open('bj1357.txt', 'r')  

T = int(input())

for i in range(T) :
    a, b = list(input().split())       # '001'의 경우 int()를 사용하면 1이 나옴. 

    a = a[::-1]
    b = b[::-1]
    
    result = str(int(a) + int(b))         # 마지막에 한 번 더 뒤집기 위해서, 더하고 str으로 만듬
    print(int(result[::-1]))            
    

