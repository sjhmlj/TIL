import sys
sys.stdin = open('bj2615.txt', 'r')

dxy = [1, 2, 3, 4]

ground = [list(input().split()) for i in range(19)]
start = []
game = 0
answer = False
for i in range(19) :
    for j in range(19) :
        if ground[i][j] != '0' :
            dol = ground[i][j]
            cnt = 1
            # 가로 보기
            for k in range(4) :
                nj = j + dxy[k]

                if nj <= 18 :
                    if ground[i][nj] == dol :
                        cnt += 1
                    
                    else : 
                        cnt = 0
                        break
                
            
            if j + 5 <= 18 and ground[i][j+5] == dol :
                    cnt = 0
                    
            if j-1 > -1 :
                if ground[i][j-1] == dol :
                    cnt = 0
            if cnt == 5 :
                answer = True
                game = dol
                start.append((i, j))
                break
            cnt = 1
            #세로보기
            for k in range(4) :
                ni = i + dxy[k]

                if ni <= 18 :
                    if ground[ni][j] == dol :
                        cnt += 1
                        
                    else : 
                        cnt = 0
                        break
            
            if i + 5 <= 18 and ground[i+5][j] == dol :
                cnt = 0
                        
            if i-1 >-1 :
                if ground[i-1][j] == dol : 
                    cnt = 0
            if cnt == 5 :    
                game = dol 
                answer = True
                start.append((i, j))
                break
            cnt = 1
            #대각선보기1 - 오른쪽 아래
            for k in range(4) :
                ni = i + dxy[k]
                nj = j + dxy[k]
                if nj <= 18 and ni <= 18 :
                    if ground[ni][nj] == dol :
                        cnt += 1
                        
                    else : 
                        cnt = 0
                        break
            
            if j + 5 <= 18 and i + 5 <= 18 :
                if ground[i+5][j+5] == dol :
                    cnt = 0
                    
            if j-1 > -1 and i-1 > -1 :
                if ground[i-1][j-1] == dol : 
                    cnt = 0
            if cnt == 5 :    
                game = dol
                answer = True
                start.append((i, j))
                break
            cnt = 1›
            #대각선보기2 - 왼쪽 아래
            for k in range(4) :
                
                ni = i + dxy[k]
                nj = j - dxy[k]
                if 0 <= nj <= 18 and 0 <= ni <= 18 :
                    if ground[ni][nj] == dol :
                        cnt += 1
                        # print(cnt)
                    else : 
                        cnt = 0
                        break
            
            if j - 5 <= 18 and i + 5 <= 18 :
                if ground[i+5][j-5] == dol :
                    cnt = 0
                    
            if j+1 <= 18 and i-1 >= 0 :
                if ground[i-1][j+1] == dol : 
                    cnt = 0
            if cnt == 5 :    
                game = dol
                answer = True
                start.append((i+4, j-4))
                break
        
    if answer == True : 
        break
if answer == True :
    print(game)
    print(start[0][0]+1, start[0][1]+1)
else :
    print(0)
                