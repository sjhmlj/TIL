import sys

sys.stdin = open("input_1288.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    num = int(input())
    mul_num = 0
    num_list = list(map(str,[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

    while True :
        mul_num += 1
        new_num = mul_num * num
        for i in str(new_num) :
        
            if i in num_list :
                num_list.remove(i)
        if num_list == [] :
            break
    print(f'#{test_case} {new_num}')