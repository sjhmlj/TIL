import sys
sys.stdin = open('swea1983.txt', 'r')

gradedic = {
    1 : 'A+',
    2 : 'A0',
    3 : 'A-',
    4 : 'B+',
    5 : 'B0',
    6 : 'B-',
    7 : 'C+',
    8 : 'C0',
    9 : 'C-',
    10 : 'D0'
}

T = int(input())

for t in range(1, T+1) :
    n, k = list(map(int, input().split()))
    score= []
    save = []
    for i in range(n) :
        a, b, c = list(map(int, input().split()))
        pscore = (a*35)+(b*45)+(c*20)
        save.append([pscore, i])
        score.append(pscore)
    score.sort(reverse = True)
    # print(save)

    for index_ in range(len(score)) :
        for j in save :
            if score[index_] == j[0] and j[1] == (k-1):
                num = index_+1
                # print(num)
                break
    
    for i in range(10) :
        seq = n / 10
        
        if num <= i*seq :
            print(f'#{t} {gradedic[i]}')
            # print(num, n, i, seq)
            break
    # # print(save, score, sep = '\n')
    # if t == 3 :
    #     for i in range(1, 11) :
    #         seq = int(n / 10)
            
    #         if num <= i*seq :
    #             print(gradedic[i])
    #             print(num, n, i, seq)
    #             break
    # print(save, score, sep = '\n')
    
    # break
    
#1 A-
#2 C-
#3 C0
#4 A-
#5 C0
#6 A-
#7 C+
#8 C+
#9 B0
#10 A0

    
    
