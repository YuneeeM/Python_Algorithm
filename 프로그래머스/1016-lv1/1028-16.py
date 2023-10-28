# 콜라 문제
def solution(a, b, n):
    answer = 0
    while n >= a:
        answer += (n//a)*b
        mod = n % a
        n = (n//a)*b
        if n+mod < a:
            break
        else:
            n = n+mod

    return answer
