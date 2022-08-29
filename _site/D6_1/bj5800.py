import sys
sys.stdin = open('bj5800.txt', 'r')

T = int(input())

for t in range(1, T+1) :
    # list_ = list(input().split())        #! str으로 sort해서 100이 제대로 정렬 안됨
    list_ = list(map(int,input().split()))       

    list_.pop(0)
    result = 0
    list_.sort()
    for i in range(len(list_)-1) :
        gap = abs(int(list_[i]) - int(list_[i+1]))
        if gap > result :
            result = gap
    # print(list_)
    print(f'Class {t}')
    print(f'Max {max(list_)}, Min {min(list_)}, Largest gap {result} ')