def solution(s) :

    answer = s
    engdic = {
        'zero' : 0,
        'one' : 1,
        'two' : 2,
        'three' : 3,
        'four' : 4,
        'five' : 5,
        'six' : 6,
        'seven' : 7,
        'eight' : 8,
        'nine' : 9
    }
    keys_ = engdic.keys()
    # return keys_             # dict_keys(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])
    for i in keys_ :
        if i in s :
            answer = answer.replace(i, str(engdic[i]))
            # answer.replace(elem, engdic[elem])
    return answer

print(solution(input()))