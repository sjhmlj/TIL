s, k, h = map(int, input().split())

result = s + k + h

if result >= 100 :
    print('OK')

else :
    num = min(s, k, h)
    if num == s :
        print('Soongsil')
    elif num == k :
        print('Korea')
    else :
        print('Hanyang')