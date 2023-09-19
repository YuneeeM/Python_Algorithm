# 문자열 뒤집기

def solution(my_string):
    answer = ''
    n = len(my_string)
    n = n+1
    for i in range(-1, -n, -1):
        answer += my_string[i]
        print(answer)
    return answer
