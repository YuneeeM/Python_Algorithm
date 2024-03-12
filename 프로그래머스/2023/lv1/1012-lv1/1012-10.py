# 정수 제곱근 판별
def solution(n):
    answer = 0
    if n ** (0.5) == int(n**0.5):
        n = n**(0.5)
        answer = (n+1)**2
    else:
        answer = -1
    return answer
