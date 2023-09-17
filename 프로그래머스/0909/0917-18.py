# 피자 나눠 먹기 (3)
def solution(slice, n):
    for i in range(1, 101):
        if slice*i >= n:
            return i
