# 피자 나눠 먹기(2)
def solution(n):
    for i in range(1, 101):
        res = i * 6
        if res % n == 0:
            return res//6
