# 합성수 찾기
def su(x):
    cnt = 0
    for i in range(1, x+1):
        if x % i == 0:
            cnt += 1
        if cnt == 3:
            break
    return cnt


def solution(n):
    answer = 0
    for i in range(1, n+1):
        if su(i) == 3:
            answer += 1

    return answer
