# 자릿수 더하기
def solution(n):
    answer = 0

    n = [x for x in str(n)]

    for x in n:
        answer += int(x)

    return answer
