# 숨어있는 숫자의 덧셈 (2)
def solution(my_string):

    answer = 0

    for x in my_string:
        if x.isalpha():
            my_string = my_string.replace(x, ' ')

    my_string = my_string.split()

    for x in my_string:
        answer += int(x)

    return answer
