# 대문자와 소문자
def solution(my_string):
    answer = ''
    for x in my_string:
        if ord(x) >= 65 and ord(x) <= 90:
            answer += x.lower()
        else:
            answer += x.upper()
    return answer
