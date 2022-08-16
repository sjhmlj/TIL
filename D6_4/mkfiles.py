import sys
sys.stdin = open('test.txt', 'r')

result = 'touch '

while True :
    try : 
        a = input()
        a = a + '.py '
        result += a

    except :
        break

print(result)



## bj는 풀고 나서 직접 붙여