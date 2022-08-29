from re import L
import sys
sys.stdin = open('swea1209.txt', 'r') 

for i in range(10) :
    test_case = int(input())
    array = []


    for k in range(100) :
        array1 = list(map(int, input().split()))
        array.append(array1)
    
   
    everything = []
    cross_sample1 = 0
    cross_sample2 = 0
    for i in range(100) :
        everything.append(sum(array[i]))
        vertice_sample = 0
        for j in range(100) :
            vertice_sample += array[i][j]
        everything.append(vertice_sample)
            
        cross_sample1 += array[i][i]
        cross_sample2 += array[-i-1][-i-1]

    everything.append(cross_sample1)
    everything.append(cross_sample2)
    print(max(everything))
