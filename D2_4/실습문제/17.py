
word = list(input())         ## 그냥 스트링으로 진행하면 훨씬 깔끔한 코드가 나오네
word_new =''
for i in range(len(word)) :
    
    word_new += chr(ord(str(word[i]))-32)   
print(word_new)
