import sys
sys.stdin = open('bj9012.txt', 'r')



for i in range(2) :

    N = int(input())               ## ')'를 스택으로 쌓고, '('이 나오면 스택에서 ')'를 뺀다.
    for i in range(N) :
        input_ = list(input())
        stack = []                ## 여기에 ')'를 넣을 것이다.
        

        for a in range(len(input_)) :    ## 모든 ')'와 '('에 대해서

            if input_.pop() == ')' :
                stack.append(')')
            else :
                if stack != [] :         ## ')'이 바깥쪽에 없는데 '('이 나온다면 틀린 예시다.
                    stack.pop()
                else : 
                    stack.append(1)     ## 마지막에 스택이 비었냐 안비었냐를 비교해서 정답을 낼거기 때문에 스택에 아무거나 하나 넣어줬다.
                    # print(stack)
                    break

        if stack == [] :
            print('Yes')           ##  Yes가 아니라 YES 다. 이걸로 시간 많이 날렸다.
        else :
            print('No')

    print('----')