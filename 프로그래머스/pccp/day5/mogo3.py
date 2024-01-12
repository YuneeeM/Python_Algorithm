# [PCCP 모의고사 #1] 3번 - 유전법칙
def gene(gen, n):
    # 1세대라면, Rr
    if gen == 1:
        return "Rr"
    # 부모를 찾아보아요
    parent = gene(gen-1, (n-1)//4+1)  # 내 윗세대, 윗세대는 몇번째 후손인가욤

    if parent == "RR" or parent == "rr":
        return parent
    if n % 4 == 0:
        return "rr"
    elif n % 4 == 1:
        return "RR"
    else:
        return "Rr"


def solution(queries):
    answer = []

    # 여러 질문마다의 결과
    for i in queries:
        answer.append(gene(i[0], i[1]))

    return answer
