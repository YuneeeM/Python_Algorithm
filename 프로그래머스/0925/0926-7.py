# 중복된 문자 제거
def solution(my_string):
    answer = ''
    for x in my_string:
        if x in str(answer):
            continue
        answer += x
    return answer
