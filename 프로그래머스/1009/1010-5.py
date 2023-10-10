# 문자열 밀기

def solution(A, B):

    if A == B:
        return 0

    n = len(A)
    cnt = 0

    for _ in range(n):
        temp = A[-1]
        temp = temp+A[:-1]
        A = temp
        cnt += 1
        if A == B:
            return cnt
    else:
        return -1
