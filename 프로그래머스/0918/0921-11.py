# 양꼬치
def solution(n, k):
    answer = 0
    if n//10 > 0:
        res = n//10
        k = k-res
        answer = n*12000+k*2000
    else:
        answer = n*12000 + k*2000

    return answer
