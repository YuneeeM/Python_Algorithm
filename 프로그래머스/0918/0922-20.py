# 구슬을 나누는 경우의 수

def solution(balls, share):
    answer = 1
    res = 1
    for i in range(1, share+1):
        if i == share+1:
            break
        answer *= balls
        i += 1
        balls -= 1
    for j in range(1, share+1):
        res *= j
    answer = answer // res
    return answer
