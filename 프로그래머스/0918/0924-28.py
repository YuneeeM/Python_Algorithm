# 팩토리얼
def solution(n):
    answer = 1
    for i in range(1, 11):
        answer *= i
        if n <= answer:
            if n != answer:
                return i-1
            return i
