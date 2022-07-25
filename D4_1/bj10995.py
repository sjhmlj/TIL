num = input()

for i in range(int(num)):
    result_line = '* '* int(num)
    if i % 2 == 1 :
        print(result_line[::-1])
    else :
        print(result_line)
