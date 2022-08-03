import sys

sys.stdin = open('bj5622.txt', 'r')  

for i in range(2) :
    input_ = input()
    result = 0
    for i in input_ :
        if ord(i) < 83 :
            wordnum = ord(i)-65             ##  'A'의 숫자를 0으로 만들고 시작. 
            result += (wordnum // 3) +3     ## 실제로 'A' 는 3초가 걸리므로 +3
        else :                  ## s 부터 룰이 바뀜. 'stuv'', 'wxyz'로 묶고, 's'는 예외처리
            if ord(i) == 83 :
                result += 8
            else :    
                wordnum2 = ord(i)-65-18  ## 's'의 숫자를 0으로 세팅
                result += (wordnum2 // 4) + 9
    print(result)