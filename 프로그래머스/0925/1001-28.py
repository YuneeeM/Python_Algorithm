# 문자열 정렬하기 (2)
def solution(my_string):
    answer = ''
    my_string = [word.lower() for word in my_string]
    my_string.sort()
    for x in my_string:
        answer += x
    return answer
