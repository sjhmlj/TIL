import sys          ##! 동원님 바이러스 풀이. 상당하다. 
sys.stdin = open('bj2606.txt', 'r')

C = int(input())
P = int(input())
matrix = [[] for _ in range(C + 1)]
result = [1]
for _ in range(P):                  # 인접 리스트 작성
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)             # [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]

switch = True                       # while문을 중단시킬 수 있는 스위치로 불리언타입 선언
k = 0
while switch:                       
    len_result = len(result)        # 다른 변수로 미리 결과리스트의 길이 할당
    for i in result:                # 결과리스트의 데이터들을 인접 리스트의 인덱스로 사용
        print(result, k, i)
        for j in matrix[i]:         # 사용된 인덱스로 뽑아낸 리스트를 순회
            if j not in result:     # 순회하며 결과리스트에 없는 값을 찾으면
                result.append(j)    # 결과값에 추가
    if len(result) == len_result:   # 어느순간, 순회하며 추가한 결과리스트와 추가하기 전 결과리스트가 차이가 없는 때가 생김
        switch = False              # 그 순간이 while문을 중단해야 되는 타이밍
    k+= 1
print(len(result) - 1)              # 결과리스트에는 1번 컴퓨터가 포함되어 있으므로 제거 후 길이 출력