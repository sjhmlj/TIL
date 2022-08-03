import sys

sys.stdin = open('bj2941.txt', 'r')              


croatialist = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in range(5) :
     
    inputlist = list(input())          #!!!! 너무 많이 틀렸다. 예외 케이스를 생각못했다..
    cnt = 0
    while inputlist :
        if inputlist[-1] == '=' :
            inputlist.pop()
            if inputlist[-1] == 'z' :
                inputlist.pop()
                
                if inputlist == []:
                    cnt += 1
                    continue
                elif inputlist[-1] == 'd' :
                    inputlist.pop()
            else :
                inputlist.pop()
            
        elif inputlist[-1] == 'j' :
            inputlist.pop()
            if inputlist == [] :
                cnt +=1 
                continue
            else :
                if inputlist[-1] == 'l' :
                    inputlist.pop()
                elif inputlist[-1] == 'n' :
                    inputlist.pop()
                
        elif inputlist[-1] == '-' :
            inputlist.pop()
            inputlist.pop()
            
        else :
            inputlist.pop()
            
        cnt += 1
    print(cnt)