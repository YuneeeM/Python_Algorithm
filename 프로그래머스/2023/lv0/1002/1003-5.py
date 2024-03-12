# 직사각형 넓이 구하기

def solution(dots):
    x = max(dots)[0] - min(dots)[0]
    y = max(dots)[1] - min(dots)[1]

    return x*y
