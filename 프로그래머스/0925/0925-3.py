# 숨어있는 숫자의 덧셈 (1)
def solution(my_string):
    answer = 0
    for x in my_string:
        if x.isdecimal():
            answer += int(x)
    return answer
