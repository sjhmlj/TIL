# def solution(numbers):
#     answer = []
#     for i in range(len(numbers)) :
#         for j in range(i+1, len(numbers)) :
#             answer.append(numbers[i]+numbers[j])
#     answer.sort()    
    
#     return list(set(answer))         ##!  이거 실패 경우가 있다. set()을 하면서 순서가 바뀌는 경우가 있는 것 같다. 

def solution(numbers):
    answer = []
    for i in range(len(numbers)) :
        for j in range(i+1, len(numbers)) :
            answer.append(numbers[i]+numbers[j])
       
    
    return sorted(list(set(answer)))