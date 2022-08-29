import sys
sys.stdin = open('bj1543.txt', 'r')

filename = input()

word = input()

a = filename.replace(word, '#')

print(a.count('#'))
print(a)