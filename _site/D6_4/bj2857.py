
answer = False
for i in range(5) :
    name = input()

    if 'FBI' in name :
        answer = True
        print(i+1)

if answer == False :
    print('HE GOT AWAY!')