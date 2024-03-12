# 제곱수 판별하기
def solution(n):
    for i in range(1, 1000001):
        if n < i**2:
            return 2
        if n == i**2:
            return 1
