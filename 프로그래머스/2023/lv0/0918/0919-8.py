# 문자 반복 출력하기
def solution(my_string, n):
    answer = ''
    for x in my_string:
        answer += (x*n)
    return answer
