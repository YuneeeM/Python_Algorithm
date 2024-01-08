# 반지
def solution(wordfind, N, ring):
    answer = 0
    # find() 없으면 -1
    # in 연산자
    for i in ring:
        if wordfind in i*2:
            answer += 1
    return answer
