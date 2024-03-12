# 정수 내림차순으로 배치하기
def solution(n):
    answer = ""
    n = [x for x in str(n)]
    n.sort(reverse=True)
    for x in n:
        answer += x

    return int(answer)
