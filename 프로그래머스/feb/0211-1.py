# 등차수열의 특정한 항만 더하기

def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i]:
            answer += (a+d*i)
            
    return answer

def solution(a, d, included):
    ai = a
    answer = 0
    for i in included:
        if i:
            answer += ai
        ai = ai + d
            
    return answer