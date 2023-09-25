# 문자열 정렬하기 (1)
def solution(my_string):
    answer = []
    for x in my_string:
        if x.isdecimal():
            answer.append(int(x))
    answer.sort()
    return answer
