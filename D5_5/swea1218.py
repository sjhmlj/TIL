import sys
sys.stdin = open('swea1218.txt', 'r')

for i in range(1, 11) :
    t = int(input())

    brackets = list(input())
    stack = []
    lbra = ['(', '[', '{', '<']
    rbra = [')', ']', '}', '>']

    its = True
    for j in brackets :
        # print(j)
        if j in lbra :
            stack.append(j)
            # print(stack[-1])
        else :
            for k in range(4) :
                if j == rbra[k] :
                    idx = k
                    break
            
            if stack[-1] == lbra[idx] :
                stack.pop()
            else :
                its = False
                break
        


                # if j == rbra[k] :
                #     if stack[-1] == lbra[k] :
                #         stack.pop()
                #         print(2)
                #         break
                # else :
                #     its = False
                #     print(0)
                #     break
        if its == False :
            break
    if stack == [] and its == True:
        print(f'#{i}', 1)
    else :
        print(f'#{i}', 0)


    # break