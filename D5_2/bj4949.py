import sys
sys.stdin = open('bj4949.txt', 'r')

from collections import deque

# line = 'So when I die (the [first] I will see in (heaven) is a score list).'
# # line = list(line)
# line = deque(line)
# print(line[-1])
for i in range(8) :
    line = deque(input())

    stack =[]
    # print(line)
    lsbra = '('
    rsbra = ')'
    lbbra = '['
    rbbra = ']'
    if line != deque(['.']) : 
        
        
    # print(line)
        answer = 'yes'
        while len(line) :
            first = line.popleft()
            if first == lsbra or first == lbbra :
                
                stack.append(first)
            elif first == rsbra :
                if stack != [] and stack[-1] == lsbra:
                    stack.pop()
                    
                else :
                    answer = 'no'
                    break
            elif first == rbbra :
                if stack != [] and stack[-1] == lbbra:
                    stack.pop()
                else :
                    answer = 'no'
                    break 

        if stack != [] :
            answer = 'no'

        print(answer)   
    