word = input()
cnt = -1
for i in word :
    cnt += 1
    if i == 'a' :
        cnt += 1
        print(cnt-1)
        break
    
if cnt == len(word)-1 :
    print(-1)