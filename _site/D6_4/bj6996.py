import sys
sys.stdin = open('test.txt', 'r')

T = int(input())

for t in range(T) :
    A, B = input().split()
    C = B

    if len(A) != len(B) :
        print(f'{A} & {B} are NOT anagrams.')
    
    else :
        for elem in A :
            C = C.replace(elem, '', 1)

        if not C :
            print(f'{A} & {B} are anagrams.')
        else :
            print(f'{A} & {B} are NOT anagrams.')