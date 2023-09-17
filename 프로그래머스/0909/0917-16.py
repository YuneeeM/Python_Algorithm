# 피자 나눠 먹기(1)
def solution(n):
    if n % 7 > 0:
        if n <= 7:
            return 1
        else:
            return (n//7)+1
    else:
        return n//7
